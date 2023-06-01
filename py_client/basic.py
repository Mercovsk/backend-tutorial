import requests

endpoint = "http://localhost:8000/api/"

# get_response = requests.get(endpoint, json={"product_id": 123})
get_response = requests.post(endpoint, json={
    'title': "Mouse Pad",
    'content': "This is a mouse pad",
    'price': 30.5
})
# print(get_response.headers)
# print(get_response.text)
# print(get_response.status_code)
print(get_response.json())