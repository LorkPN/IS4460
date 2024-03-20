import requests

id = 2

api_url = f'http://127.0.0.1:8000/api/customers/{id}/'

response = requests.get(api_url)

if response.status_code == 200:
    customer_data = response.json()
    print(customer_data)
else:
    print(f"Error retrieving the customer: status code {response.status_code}")