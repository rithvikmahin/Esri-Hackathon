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

url = "https://open.spotify.com/playlist/6Oo1h6XVJSh3TKATxgUkF7?si=ecf2f522e75844e9"

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

print(Dict)

# print(artistCountries)
# quit()


# artistsCountry = artistIDs
# for eachArtist in artists:
#     print(eachArtist)

quit()
############################################





### old script
# artist_id = tracks["items"][0]["track"]["artists"][0]["id"]
# related_artists = sp.artist_related_artists(artist_id)
### end old script


# get the name and country/area of artist(s) from your playlist
# musicbrainzngs.set_useragent("test", "1")
# query = musicbrainzngs.search_artists(query=artist)
# country = query["artist-list"][0]["country"]
# print("Artists in your playlist: \n\t\t" + artist,",",country)


# #get related artists' name
# x = 1
# print("Top 3 Related artists")
# for i in related_artists["artists"]:
#     if x < 3:
#         print("Related Artists " + str(x) +": \t"+ i["name"])
#         # not sure what would happen if there are less than 3 geners
#         print("\t" + "Top 3 genres: " + str(i["genres"][0:3]))   
#         x += 1
#         musicbrainzngs.set_useragent("test","1")
#         queryBranch = musicbrainzngs.search_artists(query=i["name"])
#         print("\tCountry: " + queryBranch["artist-list"][0]["country"])
#         #print all information
#         #print(i)
#     else:
#         break


# symbology later on
# county in red -- favorite srtists
# county in dark 
# full story pitch
