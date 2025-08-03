import requests
from bs4 import BeautifulSoup
import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from pathlib import Path


load_dotenv()
client_id = os.getenv('SPOTIFY_CLIENT_ID')
client_secret = os.getenv('SPOTIFY_CLIENT_SECRET')
redirect_uri = "https://example.com/"


date = input("Chose a date to create top 100 hits, type the date in this format YYYY-MM-DD: ")
url = "https://www.billboard.com/charts/hot-100/"
response = requests.get(url=f"{url}{date}")
soup = BeautifulSoup(response.text, 'html.parser')

top_song_list = soup.select("li ul li h3.c-title")
song_names = [song.getText().strip() for song in top_song_list]


# spotify authentication
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=client_id,
        client_secret=client_secret,
        redirect_uri=redirect_uri,
        scope="playlist-modify-private",
        cache_path="token.txt",
    )
)
user_id = sp.current_user()["id"]


# search for top100 songs from a given date
Path("uris").mkdir(exist_ok=True)
file_path = f"uris/{date}.txt"

if Path(file_path).exists():
    with open(file_path, "r") as file:
        song_uris = file.read().splitlines()
else:
    song_uris = []
    search_date = date[:4]
    print("Getting song URIs...")
    for song in song_names:
        song_response = sp.search(
            q=f"track: {song} year: {search_date}",
            type="track",
            limit=1,
        )
        try:
            song_uri = song_response["tracks"]["items"][0]["uri"]
            song_uris.append(song_uri)
        except IndexError:
            print(f"{song} not found")
    with open(file_path, "w") as f:
        f.write("\n".join(song_uris))


# create and fill playlist
playlist = sp.user_playlist_create(
    user=user_id,
    name=f"{date} Billboard 100",
    public=False,
)

playlist_id = playlist["id"]

sp.playlist_add_items(
    playlist_id=playlist_id,
    items=song_uris,
)



