import requests
import json

id = 1

api_url = f'http://127.0.0.1:8000/api/orders/{id}/'

response = requests.delete(api_url)

if response.status_code == 204:
    print("Order deleted successfully")
else:
    print(f"Error deleting the order: status code {response.status_code}")