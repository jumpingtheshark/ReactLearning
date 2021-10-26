import requests

client_id = "3032d7618ce34dffaf349214bba92cd5"
client_secret = "a6bf34e7fc4b4066991b3d344f465a3f"


BASE_URL = 'https://api.spotify.com/v1/tracks/2TpxZ7JUBn3uw46aR7qd6V'
BASE_URL = 'https://api.spotify.com/v1/artists/6hKLYGlOtGVNzZUuvS99Nw/top-tracks?market=ES' #vysotsky

#scope = "appstore::apps:readwrite"
grant_type = "client_credentials"
data = {
    "grant_type": grant_type,
    "client_id": client_id,
    "client_secret": client_secret,

}
#auth_url = "https://api.amazon.com/auth/o2/token"
auth_url = "https://accounts.spotify.com/api/token"

auth_response = requests.post(auth_url, data=data)

# Read token from auth response
auth_response_json = auth_response.json()
auth_token = auth_response_json["access_token"]

auth_token_header_value = "Bearer %s" % auth_token

auth_token_header = {"Authorization": auth_token_header_value}
print (auth_token)

r= requests.get (BASE_URL, headers={ 'Authorization': 'Bearer '+ auth_token})
rjson=r.json()
print (rjso
