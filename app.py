from dotenv import load_dotenv, find_dotenv
import requests
import os
import random

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
fav_artists = ["5xeBMeW0YzWIXSVzAxhM8O", "1OKOTYGoCE2buxTYMegJp7", "72rZmJbRFSY6IFJAysfOdr"]
BASE_URL = "https://api.spotify.com/v1/artists"

response = requests.get(BASE_URL, params={
    "access_token" : access_token,
    "id" : fav_artists[random.randint(0,2)]
})

data = response.json()