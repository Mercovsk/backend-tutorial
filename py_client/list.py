import requests

endpoint = "http://localhost:8000/api/products/"

data = {
    "title": "GPU",
    "price": 11999.50
}

get_response = requests.get(endpoint)

print(get_response.json())