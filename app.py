from dotenv import load_dotenv, find_dotenv
import requests
import os
import random
from flask import Flask, render_template



app = Flask(__name__)

@app.route('/')
def index():
    # Get access token
    load_dotenv(find_dotenv())
    AUTH_URL = "https://accounts.spotify.com/api/token"
    
    auth_response = requests.post(AUTH_URL, {
        'grant_type': 'client_credentials',
        'client_id' : os.getenv('SPOTIFY_CLIENT'),
        'client_secret' : os.getenv('SPOTIFY_KEY')
    })
    
    auth_response_data = auth_response.json()
    access_token = auth_response_data['access_token']
    
    
    # Choose an artist and fetch their top tracks
    fav_artists = ["5xeBMeW0YzWIXSVzAxhM8O", "1OKOTYGoCE2buxTYMegJp7", "4Mt6w4tDGiPgV5q6JWPlrI", "5rx7lpIuya41ws2oWXRiGu"]
    id = fav_artists[random.randint(0,len(fav_artists) - 1)]
    BASE_URL = "https://api.spotify.com/v1/artists/" + id + "/top-tracks"
    
    response = requests.get(BASE_URL, params={
        "access_token" : access_token,
        "market" : "US"
    })
    data = response.json()
    
    #extract the relevant info from the resulting JSON
    song = data["tracks"][random.randint(0, len(data["tracks"])-1)]
    song_name = song["name"]
    artist = song["album"]["artists"][0]["name"]
    song_image=song["album"]["images"][0]["url"]
    preview_url=song["preview_url"]
    
    #Genius API
    GENIUS_URL = 'https://api.genius.com/search'
    genius_response = requests.get(GENIUS_URL, params = {
        'q' : song_name
        }, 
        headers = {
        'Authorization' : 'Bearer ' + os.getenv('CLIENT_ACCESS_TOKEN')
        }
    )
    
    genius_data = genius_response.json()
    genius_URL = genius_data['response']['hits'][0]['result']['url']
    
    return render_template("index.html", song_name=song_name, artist=artist, song_image=song_image, preview_url=preview_url, genius_URL=genius_URL)


app.run(
    port=int(os.getenv('PORT', 8080)),
    host=os.getenv('IP', '0.0.0.0')
)