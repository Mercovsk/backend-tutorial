import requests

endpoint = "http://localhost:8000/api/products/"

data = {
    "title": "GPU",
    "price": 11999.50
}

get_response = requests.post(endpoint, json=data)

print(get_response.json())