from flask import Flask, request
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
    musicbrainzngs.set_useragent("test","1")

    # a dictionary {"name of artist" : "times appear in the playlist"}
    artistList = {}
    artistIDs = {}
    artistCountries = {}

    Dict = {}

    for song in tracks["items"]:
        artists = song["track"]["artists"]

        for artist in artists:
            if artist["name"] not in artistList:
                # create artist and start counting as 1
                artistList[artist["name"]] = 1
                artistIDs[artist["name"]] = artist["id"]
                # get the country info of artist
                queryBranch = musicbrainzngs.search_artists(query=artist["name"])
                if "country" in queryBranch["artist-list"][0].keys():
                    # artistCountries[artist["name"]] = queryBranch["artist-list"][0]["country"]

                    newArtist = {"id":artist["id"], "country/area":queryBranch["artist-list"][0]["country"],"count":1}

                elif "area" in queryBranch["artist-list"][0].keys():
                    # artistCountries[artist["name"]] = queryBranch["artist-list"][0]["area"]["name"]

                    newArtist = {"id":artist["id"], "country/area":queryBranch["artist-list"][0]["area"]["name"],"count":1}

                else:
                    #pass for now
                    continue

                Dict[artist["name"]] = newArtist

            else:
                # artistList[artist["name"]] += 1
                Dict[artist["name"]]["count"] +=1
                
    # all artists' info is stored in Dict
    print("Here2")
    print("Dict, ", Dict)

    # print(artistCountries)
    # quit()


    # artistsCountry = artistIDs
    # for eachArtist in artists:
    #     print(eachArtist)

    quit()
    return Dict

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)