import requests
import json

id = 2

api_url = f'http://127.0.0.1:8000/api/customers/{id}/'

response = requests.delete(api_url)

if response.status_code == 204:
    print("Customer deleted successfully")
else:
    print(f"Error deleting the customer: status code {response.status_code}")