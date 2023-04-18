import requests


"""Показать какие заголовки мы передали с запросом"""
headers = {"some_headers" :"123"}
response = requests.get("https://playground.learnqa.ru/api/show_all_headers", headers=headers)
"""Заголовки, которые получил сервер в запросе от клиента"""
print(response.json())
"""Ответ сервера на запрос"""
print(response.headers)
print("="*50)

"""Получение кукиз"""
payload = {"login" : "secret_login", "password" : "secret_pass"}
response = requests.post("https://playground.learnqa.ru/api/get_auth_cookie", data=payload)
print(response.text)
print(response.status_code)
print(dict(response.cookies))
print(response.headers)
print("="*50)
"""Неправильный пароль"""
payload = {"login" : "secret_login", "password" : "secret_pass2"}
response = requests.post("https://playground.learnqa.ru/api/get_auth_cookie", data=payload)
print(response.text)
print(response.status_code)
print(dict(response.cookies))
print("="*50)
"""Передача полученных куки в последующих запросах"""
payload = {"login" : "secret_login", "password" : "secret_pass"}
# payload = {"login" : "secret_login", "password" : "secret_pass1"}
get_response = requests.post("https://playground.learnqa.ru/api/get_auth_cookie", data=payload)

cookies_value = get_response.cookies.get('auth_cookie')
cookies = {}
if cookies_value is not None:
    cookies.update({'auth_cookie': cookies_value})

response = requests.post("https://playground.learnqa.ru/api/check_auth_cookie", cookies=cookies)
print(response.text)
print("="*50)