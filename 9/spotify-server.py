#https://flask.palletsprojects.com/en/2.0.x/quickstart/
import flask
from flask_cors import CORS
from flask import Flask, request, jsonify, session
from datetime import date
import requests
import logging
import json
import sys


app = Flask(__name__)
CORS(app)


#https://jsonplaceholder.typicode.com/todos
#http://json.parser.online.fr/



@app.route("/",  methods=['GET','POST'])
def hello_world():
   # data=request.get_json(force=True)
    print('health check', file=sys.stdout)
    return " blah"


def get_token():
    client_id = "3032d7618ce34dffaf349214bba92cd5"
    client_secret = "a6bf34e7fc4b4066991b3d344f465a3f"

    # scope = "appstore::apps:readwrite"
    grant_type = "client_credentials"
    data = {
        "grant_type": grant_type,
        "client_id": client_id,
        "client_secret": client_secret,

    }
    # auth_url = "https://api.amazon.com/auth/o2/token"
    auth_url = "https://accounts.spotify.com/api/token"

    auth_response = requests.post(auth_url, data=data)

    # Read token from auth response
    auth_response_json = auth_response.json()
    auth_token = auth_response_json["access_token"]
    return auth_token

#leonard cohen top tracks
#https://developer.spotify.com/console/get-artist-top-tracks/?id=5l8VQNuIg0turYE1VtM9zV&market=ES
#http://localhost:5001/tracks?spotify_id=5l8VQNuIg0turYE1VtM9zV&market
@app.route("/tracks",  methods=['GET','POST'])
def get_tracks():
    auth_token=get_token()
    BASE_URL = 'https://api.spotify.com/v1/artists/{id}/top-tracks?market=ES'

    spotify_id = request.args.get('spotify_id')
    BASE_URL = BASE_URL.format(id=spotify_id)
    r = requests.get(BASE_URL, headers={'Authorization': 'Bearer ' + auth_token})
    dictionary = r.json()
    tracks = dictionary["tracks"]  # tracks array
    tracks2 = []

    for track in tracks:
        tracks_json = {
            "name": track["name"],
            "preview_url": track["preview_url"]
        }
        tracks2.append(tracks_json)

    tracks_result = {"top_tracks": tracks2}
    return jsonify(tracks_result)

@app.route("/Artist",  methods=['GET','POST'])
def get_artist():


    client_id = "3032d7618ce34dffaf349214bba92cd5"
    client_secret = "a6bf34e7fc4b4066991b3d344f465a3f"

    #BASE_URL = 'https://api.spotify.com/v1/tracks/2TpxZ7JUBn3uw46aR7qd6V'
    #BASE_URL = 'https://api.spotify.com/v1/artists/6hKLYGlOtGVNzZUuvS99Nw/top-tracks?market=ES'  # vysotsky
    BASE_URL = 'https://api.spotify.com/v1/search?q={name}&type=artist&limit=2'


    # scope = "appstore::apps:readwrite"
    grant_type = "client_credentials"
    data = {
        "grant_type": grant_type,
        "client_id": client_id,
        "client_secret": client_secret,

    }
    # auth_url = "https://api.amazon.com/auth/o2/token"
    auth_url = "https://accounts.spotify.com/api/token"

    auth_response = requests.post(auth_url, data=data)

    # Read token from auth response
    auth_response_json = auth_response.json()
    auth_token = auth_response_json["access_token"]

    auth_token_header_value = "Bearer %s" % auth_token

    #auth_token_header = {"Authorization": auth_token_header_value}
    #print(auth_token)

    artist_name = request.args.get('name')
    BASE_URL=BASE_URL.format(name=artist_name)
    r = requests.get(BASE_URL, headers={'Authorization': 'Bearer ' + auth_token})
    dictionary = r.json()

    #dictionary = json.loads(rjson)

    total_followers = dictionary["artists"]["items"][0]["followers"]["total"]
    name = dictionary["artists"]["items"][0]["name"]
    spotify_id = dictionary["artists"]["items"][0]["id"]
    image_url = dictionary["artists"]["items"][0]["images"][0]["url"]
    genres=dictionary["artists"]["items"][0]["genres"]


    print(spotify_id, name, image_url, total_followers, "genres: ", genres)

    rjson2= {
            "spotify_id":spotify_id,
            "name":name,
            "image_url":image_url,
            "total_followers":total_followers,
            "genres":genres
    }



    #rjson = r.json()


    return jsonify(rjson2)




#app.run(host='0.0.0.0',port=5001)
app.run(port=5001)
