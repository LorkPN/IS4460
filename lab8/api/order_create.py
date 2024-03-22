import requests
import json

cust_id = 2
api_url = 'http://127.0.0.1:8000/api/orders/'

order_data = {
    "order_total": 777.77,
    "notes": "Minting",
    "customer_id" : cust_id,
    "status":'pending'
}

response = requests.post(url = api_url,
                         data = json.dumps(order_data),
                         headers={"Content-Type": 'application/json'})

if response.status_code == 201:
    print("Order created successfully.")
else:
    print(f"Error creating order: status code {response.status_code}")