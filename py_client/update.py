import requests

endpoint = "http://127.0.0.1:8000/api/products/13/update/"
data = {
    "title": "Gaming Mouse",
    "content": "This is a gaming mouse",
    "price": 249.99
}

get_response = requests.put(endpoint, json=data)
print(get_response.json())