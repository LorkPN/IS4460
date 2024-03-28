import requests

api_url = 'http://localhost:8000/customer/api/'

token = '615556f5b2c41e746cecf88c47bfc31822330ccf'

headers = {
    'Authorization': f'Token {token}'
}

response = requests.get(api_url, headers=headers)

if response.status_code == 200:
    print(f"Customers retrieval successful: {response.text}")
else:
    print(f"Customers retrieval failed: error code {response.status_code}")