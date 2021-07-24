# Get related artists that are not in the country
import spotipy
import musicbrainzngs

from iso3166 import countries

from spotipy.oauth2 import SpotifyClientCredentials
cid = '4335e7dec6f24bc5b85b1c015912cf5e' #our own ID
secret = '34e6b849c10d4edbb476adddf990171e'
client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

#prepare for country search
musicbrainzngs.set_useragent("test","1")

#data sample
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
        'Red Hot Chili Peppers': {'id': '0L8ExT028jH3ddEcZwqJJ5', 'country/area': 'US', 'count': 1}, 'Steve Miller Band': {'id': '6QtGlUje9TIkLrgPZrESuk', 'country/area': 'US', 'count': 1}, 'The Doors': {'id': '22WZ7M8sxp5THdruNY3gXt', 'country/area': 'US', 'count': 1}, 'R.E.M.': {'id': '4KWTAlx2RvbpseOGMEmROg', 'country/area': 'US', 'count': 1}, 'The Beach Boys': {'id': '3oDbviiivRWhXwIE8hxkVV', 'country/area': 'US', 'count': 2}, 'Dire Straits': {'id': '0WwSkZ7LtFUFjGjMZBMt6T', 'country/area': 'GB', 'count': 2}, 'Joni Mitchell': {'id': '5hW4L92KnC6dX9t7tYM4Ve', 'country/area': 'CA', 'count': 2}, 'Cass Elliot': {'id': '5jX7X3kRkfJTRqAdT7RcHk', 'country/area': 'US', 'count': 1}, 'Green Day': {'id': '7oPftvlwr6VrsViSDV7fJY', 'country/area': 'US', 'count': 2}, 'Juice Newton': {'id': '4L1z1IcfK7lbqx8izGHaw5', 'country/area': 'US', 'count': 1}, 'Elvis Costello': {'id': '2BGRfQgtzikz1pzAD0kaEn', 'country/area': 'GB', 'count': 1}, 'Jim Croce': {'id': '1R6Hx1tJ2VOUyodEpC12xM', 'country/area': 'US', 'count': 1}, 'Kendrick Lamar': {'id': '2YZyLoL8N0Wb9xBt1NhZWg', 'country/area': 'US', 'count': 1}}
 
existingCountries = []
for artist in Dic.keys():
    tempPlace = Dic[artist]["country/area"]
    if tempPlace not in existingCountries:
        existingCountries.append(tempPlace)  

print(existingCountries)
print("\n----------\n")

for artist in Dic.keys():
    related_artists = sp.artist_related_artists(Dic[artist]["id"])
    relatedList = []
    for related_artist in related_artists["artists"]:
        relatedList.append(related_artist["name"])

        #print(relatedList)
    #print(related_artists["artists"][0]["name"])
    #queryBranch = musicbrainzngs.search_artists(query=related_artists["artists"][0]["name"])

        queryBranch = musicbrainzngs.search_artists(query=related_artist)
    
        place = ''
        if "country" in queryBranch["artist-list"][0].keys():
            place = queryBranch["artist-list"][0]["country"]
        elif "area" in queryBranch["artist-list"][0].keys():
            place = queryBranch["artist-list"][0]["area"]["name"]
        else:
            #pass for now
            continue
        #print(place + "  length: " + str(len(place)))
        if place != '' and place not in existingCountries:
            if len(place) < 4:
                print("hh\n" + place)
                print(queryBranch["artist-list"])
                quit()

    #check if country is in existing list
    

