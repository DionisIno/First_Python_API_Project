import requests
from json.decoder import JSONDecodeError



payload = {"name": "Denis"}
response = requests.get("https://playground.learnqa.ru/api/hello", params=payload)
parsed_response = response.json()
print(parsed_response['answer'])
print('='*50)


response = requests.get("https://playground.learnqa.ru/api/get_text", params=payload)
try:
    parsed_response_text = response.text
    print(parsed_response_text)
except JSONDecodeError:
    print("It is not a JSON format")
print('='*50)


payload = {'param1': 'value1'}
response = requests.get("https://playground.learnqa.ru/api/check_type", params=payload)
print(response.text)
print('='*50)

response = requests.post("https://playground.learnqa.ru/api/check_type", data=payload)
print(response.text)
print('='*50)

response = requests.post("https://playground.learnqa.ru/api/check_type")
print(response.status_code)
print('='*50)

response = requests.post("https://playground.learnqa.ru/api/get_500")
print(response.status_code)
print(response.text)
print('='*50)

response = requests.post("https://playground.learnqa.ru/api/get_50")
print(response.status_code)
print(response.text)
print('='*50)

response = requests.post("https://playground.learnqa.ru/api/get_301", allow_redirects=True)
all_response = response.history[0]
print(response.status_code)
print(response.url)
print(all_response.url)
print('='*50)

response = requests.post("https://playground.learnqa.ru/api/get_302")
print(response.status_code)
print(response.text)
print('='*50)