from flask import Flask, request, jsonify
from flask_cors import CORS
# This script takes a PUBLIC spotify playlist and returns the list of related artists
import spotipy
import musicbrainzngs
from spotipy.oauth2 import SpotifyClientCredentials

cid = '4335e7dec6f24bc5b85b1c015912cf5e' #our own ID
secret = '34e6b849c10d4edbb476adddf990171e'
client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# public spotify playlist links 
# from a chinese friend: "https://open.spotify.com/playlist/37i9dQZF1DWSBcxmKiZ0B8"
#                           "https://open.spotify.com/playlist/1q21zSTS47o2GZKz7rktOb"
# from charlie "https://open.spotify.com/playlist/6Oo1h6XVJSh3TKATxgUkF7?si=ecf2f522e75844e9"


app = Flask(__name__)
CORS(app)

@app.route('/api', methods = ['POST'])
def get_query_from_react():
    data = request.get_json()
    url = data["data"]
    tracks = sp.playlist_tracks(url, limit=50)
    musicbrainzngs.set_useragent("userAgent","1.0")

    artistList = {}

    Dict = {}

    for song in tracks["items"]:
        artists = song["track"]["artists"]

        for artist in artists:
            if artist["name"] not in artistList:
                # get the country info of artist
                queryBranch = musicbrainzngs.search_artists(query=artist["name"])
                if "country" in queryBranch["artist-list"][0].keys():
                    newArtist = {"id":artist["id"], "country/area":queryBranch["artist-list"][0]["country"],"count":1}

                elif "area" in queryBranch["artist-list"][0].keys():
                    newArtist = {"id":artist["id"], "country/area":queryBranch["artist-list"][0]["area"]["name"],"count":1}

                else:
                    #pass for now
                    continue

                Dict[artist["name"]] = newArtist

            else:
                # artistList[artist["name"]] += 1
                Dict[artist["name"]]["count"] +=1
                
    # all artists' info is stored in Dict
    #print("Dict, ", Dict)

    existingCountries = []
    # parse dict to get country information
    for artist in Dict.keys():
        tempPlace = Dict[artist]["country/area"]
        if tempPlace not in existingCountries:
            existingCountries.append(tempPlace)  

    print(existingCountries)
    print("\n----------")

    ## Get recommandation 
    recommendSingers = {}
    #for each artist
    for artist in Dict.keys():
        # check if we need to break
        if(len(recommendSingers) > 3):
            break

    # Related artists from Spotify
        related_artists = sp.artist_related_artists(Dict[artist]["id"])
        ## for each
        for related_artist in related_artists["artists"]:
            #print(related_artist)

            related_info = musicbrainzngs.search_artists(query=related_artist['name'])
            place = ''
        
            if "country" in related_info["artist-list"][0].keys():
                place = related_info["artist-list"][0]["country"]
            elif "area" in related_info["artist-list"][0].keys():
                place = related_info["artist-list"][0]["area"]["name"]
            else:
                #pass for now
                break
        
            if place != '' and place not in existingCountries:
                if len(place) < 4:
                    if related_artist["name"] not in recommendSingers:
                        print("New country: " + place + "\ninfo: ")
                        print(related_artist["name"])
                        recommendSingers[related_artist["name"]] = {"Place": place}
            if(len(recommendSingers) > 3):
                break   
    
    ### Get Url for each artist in recommendSingers
    if len(recommendSingers) > 1: # not empty
        for recmdArti in recommendSingers:
            print(recmdArti)
    ## end getting URL

    recommend = {}
    recommend["RecommendArtists"] = recommendSingers

    result = {}
    result["ArtistsInPlaylist"] = Dict

    ## Combine the artist in the playlist and the recommendation
    result.update(recommend)

    ##############
    ## A sample of return value:
    ## result = 
    # {'ArtistsInPlaylist': 
    #     {'Steely Dan': 
    #         {'id': '6P7H3ai06vU1sGvdpBwDmE', 'country/area': 'US', 'count': 1}, 
    #     'Van Morrison': 
    #         {'id': '44NX2ffIYHr6D4n7RaZF7A', 'country/area': 'Northern Ireland', 'count': 6}, 
    #     'Bob Dylan': 
    #         {'id': '74ASZWbe4lXaubB36ztrGX', 'country/area': 'US', 'count': 14}, 
    #     'Dire Straits': 
    #         {'id': '0WwSkZ7LtFUFjGjMZBMt6T', 'country/area': 'GB', 'count': 2}
    #     }, 
    # 'RecommendArtists': 
    #     { 
    #       'Little River Band': 'AU', 
                                    # {country: "xx", link: "xxx.com"}
    #       'The Boomtown Rats': 'IE', 
    #       'Crowded House': 'AU', 
    #       'INXS': 'AU'
    #     }
    # }
    ######################
    print("Jsonify Result", result)
    return jsonify(result)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)