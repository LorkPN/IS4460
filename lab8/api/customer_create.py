import requests
import json

api_url = 'http://127.0.0.1:8000/api/customers/'

customer_data = {
    "name": "Henry II",
    "email": "GoldenRule@gmail.com",
    "phone_number":"(020) 497-5559"
}

response = requests.post(url = api_url,
                         data = json.dumps(customer_data),
                         headers={"Content-Type": 'application/json'})

if response.status_code == 201:
    print("Customer created successfully.")
else:
    print(f"Error creating customer: status code {response.status_code}")