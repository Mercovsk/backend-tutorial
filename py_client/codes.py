# request.get(endpoint)

# {
#     'args': {}, 
#     'data': '', 
#     'files': {}, 
#     'form': {}, 
#     'headers': {
#         'Accept': '*/*', 
#         'Accept-Encoding': 'gzip, deflate', 
#         'Host': 'httpbin.org', 
#         'User-Agent': 'python-requests/2.31.0', 
#         'X-Amzn-Trace-Id': 'Root=1-646dccda-6673f98618d81ad90e6aa77d'
#     }, 
#     'json': None, 
#     'method': 'GET', 
#     'origin': '119.95.21.55', 
#     'url': 'https://httpbin.org/anything'
# }

# requests.get(endpoint, json={"query": "Hello World"})

# {
#     'args': {}, 
#     'data': '{"query": "Hello World"}', 
#     'files': {}, 
#     'form': {}, 
#     'headers': {
#         'Accept': '*/*', 
#         'Accept-Encoding': 'gzip, deflate', 
#         'Content-Length': '24', 
#         'Content-Type': 'application/json', 
#         'Host': 'httpbin.org', 
#         'User-Agent': 'python-requests/2.31.0', 
#         'X-Amzn-Trace-Id': 'Root=1-646dce56-61571c1e2a0833264f2302e6'
#     }, 
#     'json': {
#         'query': 'Hello World'
#     }, 
#     'method': 'GET', 
#     'origin': '119.95.21.55', 
#     'url': 'https://httpbin.org/anything'
# }

# requests.get(endpoint, data={"query": "Hello World"})

# {
#     'args': {}, 
#     'data': '', 
#     'files': {}, 
#     'form': {
#         'query': 'Hello World'
#     }, 
#     'headers': {
#         'Accept': '*/*', 
#         'Accept-Encoding': 'gzip, deflate', 
#         'Content-Length': '17', 
#         'Content-Type': 'application/x-www-form-urlencoded', 
#         'Host': 'httpbin.org', 
#         'User-Agent': 'python-requests/2.31.0', 
#         'X-Amzn-Trace-Id': 'Root=1-646dcef4-4bbbba6b269ba8fc38c31fa0'
#     }, 
#     'json': None, 
#     'method': 'GET', 
#     'origin': '119.95.21.55', 
#     'url': 'https://httpbin.org/anything'
# }