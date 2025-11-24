import requests
import json

url = 'http://127.0.0.1:8000/product_description'
headers = {
    'accept': 'application/json',
    'Content-Type': 'application/json'
}

payload = {
    "name": "Headphones",
    "notes": "Noise cancellation hands-free calling long battery life"
}

response = requests.post(url, headers=headers, data=json.dumps(payload))

print("STATUS:", response.status_code)
print(response.json())
