import requests
import json

id = 2
api_url = f'http://127.0.0.1:8000/api/customers/{id}/'

customer_data = {
    "name": "Henry II",
    "email": "GoldenRule@gmail.com",
    "phone_number":"(020) 133-1189"
}

response = requests.put(url = api_url,
                         data = json.dumps(customer_data),
                         headers={"Content-Type": 'application/json'})

if response.status_code == 200:
    print("Customer updated successfully.")
else:
    print(f"Error updating customer: status code {response.status_code}")