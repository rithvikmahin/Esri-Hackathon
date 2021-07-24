# This script takes a PUBLIC spotify playlist and returns the list of related artists
import spotipy
import musicbrainzngs

from spotipy.oauth2 import SpotifyClientCredentials
cid = '4335e7dec6f24bc5b85b1c015912cf5e' #our own ID
secret = '34e6b849c10d4edbb476adddf990171e'
client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# public spotify playlist link 
url = "https://open.spotify.com/playlist/37i9dQZF1DWSBcxmKiZ0B8"
tracks = sp.playlist_tracks(url, limit=1)

artist = tracks["items"][0]["track"]["artists"][0]["name"]
artist_id = tracks["items"][0]["track"]["artists"][0]["id"]
related_artists = sp.artist_related_artists(artist_id)

# get the name and country/area of artist(s) from your playlist
musicbrainzngs.set_useragent("test", "1")
query = musicbrainzngs.search_artists(query=artist)
country = query["artist-list"][0]["country"]
print("Artists in your playlist: \n\t\t" + artist,",",country)

#get related artists' name
x = 1
print("Top 3 Related artists")
for i in related_artists["artists"]:
    if x < 3:
        print("Related Artists " + str(x) +": \t"+ i["name"])
        # not sure what would happen if there are less than 3 geners
        print("\t" + "Top 3 genres: " + str(i["genres"][0:3]))   
        x += 1
        musicbrainzngs.set_useragent("test","1")
        queryBranch = musicbrainzngs.search_artists(query=i["name"])
        print("\tCountry: " + queryBranch["artist-list"][0]["country"])
        #print all information
        #print(i)
    else:
        break


