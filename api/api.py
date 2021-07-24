#Just checking the sync

import spotipy
import musicbrainzngs

from spotipy.oauth2 import SpotifyClientCredentials
cid = '4335e7dec6f24bc5b85b1c015912cf5e' #our own ID
secret = '34e6b849c10d4edbb476adddf990171e'
client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
sp = spotipy.Spotify(client_credentials_manager=
client_credentials_manager)
# public spotify playlist link 

url = "https://open.spotify.com/playlist/6Oo1h6XVJSh3TKATxgUkF7?si=ecf2f522e75844e9"
tracks = sp.playlist_tracks(url, limit=1)
artist = tracks["items"][0]["track"]["artists"][0]["name"]
artist_id = tracks["items"][0]["track"]["artists"][0]["id"]
related_artists = sp.artist_related_artists(artist_id)
print(related_artists["artists"])

musicbrainzngs.set_useragent("test", "1")
query = musicbrainzngs.search_artists(query="Taylor Swift")
country = query["artist-list"][0]["country"]
print(artist,",",country)