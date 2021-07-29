# Get related artists that are not in the country
import spotipy
import musicbrainzngs

from iso3166 import countries

from spotipy.oauth2 import SpotifyClientCredentials
cid = '' #our own ID
secret = ''
client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

#prepare for country search
musicbrainzngs.set_useragent("test","1")

#data sample
#dict = { artist1: {id: xx, country: 'xx', count"}}
Dic = {'Steely Dan': 
            {'id': '6P7H3ai06vU1sGvdpBwDmE', 'country/area': 'US', 'count': 1}, 
        'Van Morrison': 
            {'id': '44NX2ffIYHr6D4n7RaZF7A', 'country/area': 'Northern Ireland', 'count': 6}, 
        'Bob Dylan': 
            {'id': '74ASZWbe4lXaubB36ztrGX', 'country/area': 'US', 'count': 14}, 
        'Elvis Costello & The Attractions': 
            {'id': '4qmHkMxr6pTWh5Zo74odpH', 'country/area': 'GB', 'count': 1}, 
        'The Rolling Stones': 
            {'id': '22bE4uQ6baNwSHPVcDxLCe', 'country/area': 'GB', 'count': 1}, 
        'Bruce Springsteen': 
            {'id': '3eqjTLE0HfPfh78zjh6TqT', 'country/area': 'US', 'count': 8}, 
        'Queen': 
            {'id': '1dfeR4HaWDbWqFHLkxsg1d', 'country/area': 'GB', 'count': 1}, 
        'Big Brother & The Holding Company': 
            {'id': '4J69yWrKwWJgjv3DKTZcGo', 'country/area': 'US', 'count': 1}, 
        'Janis Joplin': 
            {'id': '4NgfOZCL9Ml67xzM0xzIvC', 'country/area': 'US', 'count': 1}, 
        'Red Hot Chili Peppers': 
            {'id': '0L8ExT028jH3ddEcZwqJJ5', 'country/area': 'US', 'count': 1}, 
        'Steve Miller Band': 
            {'id': '6QtGlUje9TIkLrgPZrESuk', 'country/area': 'US', 'count': 1}, 
        'The Doors': 
            {'id': '22WZ7M8sxp5THdruNY3gXt', 'country/area': 'US', 'count': 1}, 
        'R.E.M.': 
            {'id': '4KWTAlx2RvbpseOGMEmROg', 'country/area': 'US', 'count': 1}, 
        'The Beach Boys': 
            {'id': '3oDbviiivRWhXwIE8hxkVV', 'country/area': 'US', 'count': 2}, 
        'Dire Straits': 
            {'id': '0WwSkZ7LtFUFjGjMZBMt6T', 'country/area': 'GB', 'count': 2}
    }
 
existingCountries = []
recommendSingers = {}
for artist in Dic.keys():
    tempPlace = Dic[artist]["country/area"]
    if tempPlace not in existingCountries:
        existingCountries.append(tempPlace)  

print(existingCountries)
print("\n----------")

#for each artist
for artist in Dic.keys():
    # check if we need to break
    if(len(recommendSingers) > 3):
        break

    # Related artists from Spotify
    related_artists = sp.artist_related_artists(Dic[artist]["id"])
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
            if len(place) < 4 and place != "CA":
                if related_artist["name"] not in recommendSingers:
                    print("New country: " + place + "\ninfo: ")
                    print(related_artist["name"])
                    recommendSingers[related_artist["name"]] = place
        if(len(recommendSingers) > 3):
            break
    
        

                

                

    # #check if country is in existing list
    

