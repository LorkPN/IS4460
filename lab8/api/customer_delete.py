import requests
import json

id = 1

api_url = f'http://127.0.0.1:8000/api/customers/{id}/'

response = requests.delete(api_url)

if requests.status_codes == 204:
    print("Customer deleted successfully")
else:
    print(f"Error deleting the customer: status code {response.status_code}")