import requests

id = 2
api_url = f'http://127.0.0.1:8000/api/orders/{id}/'

response = requests.get(api_url)

if response.status_code == 200:
    order_data = response.json()
    print(order_data)
else:
    print(f"Error retrieving the order: status code {response.status_code}")