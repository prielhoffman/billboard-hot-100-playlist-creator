# Step 1 - Scraping the Billboard Hot 100
# 1. Create an input() prompt to ask the user for a date in YYYY-MM-DD format.
# 2. Use requests to fetch the Billboard Hot 100 page for the given date.
# 3. Parse the webpage using BeautifulSoup to extract song titles into a list.

import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Spotify API credentials
CLIENT_ID = "YOUR CLIENT ID"
CLIENT_SECRET = "YOUR CLIENT SECRET"
REDIRECT_URI = "http://example.com"
SCOPE = "playlist-modify-private"

# Prompt user for date input
date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
url = f"https://www.billboard.com/charts/hot-100/{date}/"
header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}

# Fetch and parse the Billboard page
response = requests.get(url=url, headers=header)
web_page = response.text
soup = BeautifulSoup(web_page, "html.parser")
songs = soup.select(selector="li ul li h3")

# Extract song titles
songs_list = []
for song in songs:
    title = song.get_text().strip()
    songs_list.append(title)

# Step 2 - Authentication with Spotify
# 1. Authenticate the application using SpotifyOAuth and fetch the current user's data.
# 2. Retrieve the Spotify user ID.

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                               client_secret=CLIENT_SECRET,
                                               redirect_uri=REDIRECT_URI,
                                               scope=SCOPE))
user_data = sp.current_user()
user_id = user_data["id"]

# Step 3 - Search Spotify for the Songs from Step 1
# 1. Define a function to search for Spotify song URIs using the song titles and the input year.

def get_spotify_uris(song_list, sp, year):
    song_uris = []
    for song in song_list:
        try:
            result = sp.search(q=f"track:{song} year:{year}", type="track", limit=1)
            song_uri = result["tracks"]["items"][0]["uri"]
            song_uris.append(song_uri)
        except IndexError:
            print(f"Song '{song}' doesn't exist in Spotify.")
    return song_uris

# Extract year from date and fetch Spotify URIs
year = date.split("-")[0]
spotify_uris = get_spotify_uris(songs_list, sp, year)

# Step 4 - Creating and Adding to Spotify Playlist
# 1. Create a new private playlist with the name "YYYY-MM-DD Billboard 100".
# 2. Add the Spotify song URIs to the new playlist.

playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
playlist_id = playlist["id"]
sp.playlist_add_items(playlist_id=playlist_id, items=spotify_uris)

print(f"Playlist '{date} Billboard 100' created successfully with {len(spotify_uris)} songs!")
