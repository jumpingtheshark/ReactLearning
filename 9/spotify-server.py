#https://flask.palletsprojects.com/en/2.0.x/quickstart/
import flask
from flask_cors import CORS
from flask import Flask, request, jsonify, session
from datetime import date
import requests
import logging


app = Flask(__name__)
CORS(app)

@app.route("/",  methods=['GET','POST'])
def hello_world():
   # data=request.get_json(force=True)
    return " blah"


#app.get('/artist/:name', (req, res, next) => {

#curl -X "GET" "https://api.spotify.com/v1/search?q=Bob%20Dylan&type=artist"
# -H "Accept: application/json" -H "Content-Type: application/json"
# -H "Authorization: Bearer BQAFa0S6nHoW"

# sample call http://172.31.89.85:5001/Artist?name=mick%20jagger
# spotify api call: https://developer.spotify.com/console/get-search-item/?q=Bob%20Dylan&type=artist&market=&limit=&offset=&include_external=

@app.route("/Artist",  methods=['GET','POST'])
def get_artist():
    client_id = "3032d7618ce34dffaf349214bba92cd5"
    client_secret = "a6bf34e7fc4b4066991b3d344f465a3f"

    #BASE_URL = 'https://api.spotify.com/v1/tracks/2TpxZ7JUBn3uw46aR7qd6V'
    #BASE_URL = 'https://api.spotify.com/v1/artists/6hKLYGlOtGVNzZUuvS99Nw/top-tracks?market=ES'  # vysotsky
    BASE_URL = 'https://api.spotify.com/v1/search?q={name}&type=artist'


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
    rjson = r.json()
    return jsonify(rjson)




app.run(host='0.0.0.0',port=5001)
