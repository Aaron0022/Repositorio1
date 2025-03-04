import requests

url = 'http://127.0.0.1:5000/procesar'
datos = [10, 20, 30, 40, 50]
response = requests.post(url, json={'datos': datos})
print(response.json())