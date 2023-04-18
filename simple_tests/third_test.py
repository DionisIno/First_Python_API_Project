import requests
import json
from pprint import pprint
import time

"""Парсинг JSON"""
json_text = '{"messages":[{"message":"This is the first message","timestamp":"2021-06-04 16:40:53"},{"message":"And this is a second message","timestamp":"2021-06-04 16:41:01"}]}'
data = json.loads(json_text)
pprint(data)
print(data['messages'][1]['message'])
print('='*100)
"""Длинный редирект"""
response = requests.get("https://playground.learnqa.ru/api/long_redirect", allow_redirects=True)
all_response = response.history
print(response.url)
count = 0
for i in all_response:
    print(i.url)
    count += 1
print(f"{count} redirects")
print('='*100)
"""Запросы и методы"""
"""1. Делает http-запрос любого типа без параметра method, описать что будет выводиться в этом случае"""
try:
    response = requests("https://playground.learnqa.ru/ajax/api/compare_query_type")
    print(response)
except TypeError:
    print("'module' object is not callable")
print('='*100)
"""2. Делает http-запрос не из списка. Например, HEAD. Описать что будет выводиться в этом случае"""
response = requests.head("https://playground.learnqa.ru/ajax/api/compare_query_type")
print(response)
print('='*100)
"""Делает запрос с правильным значением method. Описать что будет выводиться в этом случае."""
response = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type")
print(response.text)
print('='*100)
"""4. С помощью цикла проверяет все возможные сочетания реальных типов запроса и значений параметра method."""
dct = {"get": requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type", params={"method": "GET"}),
       "post": requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type", data={"method": "POST"}),
       "put": requests.put("https://playground.learnqa.ru/ajax/api/compare_query_type", data={"method": "PUT"}),
       "delete": requests.delete("https://playground.learnqa.ru/ajax/api/compare_query_type", data={"method": "DELETE"})}
for i in dct:
    response = dct[i]
    print(response.text)
    print(response.status_code)
print('='*100)

"""Токены"""

response = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job")
token = response.json()["token"]
seconds = response.json()["seconds"]
print(f"Task is created with token {token} and will be ready in {seconds} seconds")

response = requests.get(f"https://playground.learnqa.ru/ajax/api/longtime_job?token={token}")
status = response.json()["status"]
print(f"Status of the task with token {token} is {status}")

time.sleep(seconds)

response = requests.get(f"https://playground.learnqa.ru/ajax/api/longtime_job?token={token}")
status = response.json()["status"]
result = response.json().get("result")
print(f"Status of the task with token {token} is {status}")
if result:
    print(f"Result of the task with token {token} is {result}")

"""Подбор пароля"""
popular_passwords = ['123456', '123456789', 'qwerty', 'password', '1234567', '12345678', '12345',
                     'iloveyou', '111111', '123123', 'abc123', 'qwerty123', '1q2w3e4r',
                     'admin', 'qwertyuiop', '654321', '555555', 'lovely', '7777777',
                     'welcome', '888888', 'princess', 'dragon', 'password1', '123qwe']
payload = {"login" : "super_admin"}
password = {}
for i in popular_passwords:
    password = {"password": i}
    payload.update(password)
    response = requests.post("https://playground.learnqa.ru/ajax/api/get_secret_password_homework", data=payload)
    auth_cookie = dict(response.cookies)
    get_response = requests.post("https://playground.learnqa.ru/ajax/api/check_auth_cookie", cookies=auth_cookie)
    if get_response.text == "You are authorized":
        break
print(f"""Правильный пароль: {password["password"]}""")
