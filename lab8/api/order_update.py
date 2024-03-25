import requests
import json

id = 2
cust_id = 2
api_url = f'http://127.0.0.1:8000/api/orders/{id}/'

order_data = {
    "order_total": "777.77",
    "notes": "Minting",
    "status": "completed",
    "customer": str(cust_id)
}

response = requests.put(url = api_url,
                         data = json.dumps(order_data),
                         headers={"Content-Type": 'application/json'})

if response.status_code == 200:
    print("Order updated successfully.")
else:
    print(f"Error updating order: status code {response.status_code}")