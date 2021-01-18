import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth

load_dotenv()

SPOTIFY_BILLBOARD_CLIENT_ID = os.getenv('SPOTIFY_BILLBOARD_CLIENT_ID')
SPOTIFY_BILLBOARD_SECRET = os.getenv('SPOTIFY_BILLBOARD_SECRET')

date = input(
    "Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

response = requests.get(f"https://www.billboard.com/charts/hot-100/{date}")
response.raise_for_status()

soup = BeautifulSoup(response.text, 'html.parser')
titles = [title_tag.text for title_tag in soup.select(
    selector="ol li button span span.color--primary")]

scope = "playlist-modify-private"

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=SPOTIFY_BILLBOARD_CLIENT_ID,
        client_secret=SPOTIFY_BILLBOARD_SECRET,
        redirect_uri='http://example.com',
        scope=scope,
        open_browser=False
    )
)

user_id = sp.current_user()["id"]

year = date.split('-')[0]

uris = []
for title in titles:
    result = sp.search(f"track: {title} year: {year}")
    try:
        uri = result['tracks']['items'][0]['uri']
    except:
        pass
    else:
        uris.append(uri)

playlist = sp.user_playlist_create(
    user=user_id, name=f"{date} Billboard 100", public=False)

sp.user_playlist_add_tracks(
    user=user_id, playlist_id=playlist['id'], tracks=uris)
