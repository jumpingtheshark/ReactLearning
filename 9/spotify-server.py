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

@app.route("/",  methods=['GET','POST'])
def hello_world():
   # data=request.get_json(force=True)
    print('line 18', file=sys.stdout)
    return " blah"


#app.get('/artist/:name', (req, res, next) => {

#curl -X "GET" "https://api.spotify.com/v1/search?q=Bob%20Dylan&type=artist"
# -H "Accept: application/json" -H "Content-Type: application/json"
# -H "Authorization: Bearer BQAFa0S6nHoW"

# sample call http://172.31.89.85:5001/Artist?name=mick%20jagger
# http://localhost:5001/Artist?name=mick%20jagger
# spotify api call: https://developer.spotify.com/console/get-search-item/?q=Bob%20Dylan&type=artist&market=&limit=&offset=&include_external=

#https://jsonplaceholder.typicode.com/todos
#http://json.parser.online.fr/


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
