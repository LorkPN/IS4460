import requests

token_url = 'http://localhost:8000/api-token-auth/'

credentials = {
    'username': 'Chump',
    'password': 'H3ll0y0u'
}

response = requests.post(token_url, data=credentials)

if response.status_code == 200:
    token_data = response.json()

    print('token_data',token_data)

    token = token_data.get("token")

    if token:
        print(f"Authentication successfull. Token: {token}")
    else:
        print("Token not found.")
else:
    print(f"Athentication failed. Error code {response.status_code}")