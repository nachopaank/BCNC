import requests
import json
URL = "https://jsonplaceholder.typicode.com/albums"

response = requests.get(URL)
jsonUrl = response.json()
with open("example.json", "r") as f:
    dataTest = json.load(f)

def test_response():
    response = requests.get(URL)
    assert response.status_code == 200
    pass

def test_data():
    assert jsonUrl[:5] == dataTest[:5]
    pass

###CLIENT CREDENTIALS

#client_id = 'myid'
#client_secret = 'mysecret'
#data = {
#    'grant_type': 'client_credentials'
#}
#access_token_response = requests.post("whatever token url", data=data, auth=(client_id, client_secret))
#tokens = json.loads(access_token_response.text)
#headers = {'Authorization': 'Bearer ' + tokens['access_token']}
#responseC = requests.get(URL, headers=headers)
###AUTH CODE

#client_id = 'myid'
#client_secret = 'mysecret'
#authorization_redirect_url = 'whateverauthurl?response_type=code&client_id=' + client_id + '&redirect_uri=WHATEVERREDIRECTURI&scope=openid'
#data = {'grant_type': 'authorization_code', 'code': "WHATEVERCODE", 'redirect_uri': "WHATEVERREDIRECTURI"}
#access_token_response = requests.post("whatevertokenurl", data=data,auth=(client_id, client_secret))
#tokens = json.loads(access_token_response.text)
#headers = {'Authorization': 'Bearer ' + tokens['access_token']}
#responseA = requests.get(URL, headers=headers)

