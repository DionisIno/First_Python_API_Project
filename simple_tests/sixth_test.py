import requests
import pytest
import random

"""Тест на короткую фразу
В рамках этой задачи с помощью pytest необходимо написать тест, который просит ввести в консоли любую фразу короче 15 символов.
А затем с помощью assert проверяет, что фраза действительно короче 15 символов."""

phrase = input("Please enter a phrase shorter than 15 characters: ")
assert len(phrase) <= 15, f"""Phrase {phrase} doesn't shorter than 15 characters"""

"""Тест запроса на метод cookie

Необходимо написать тест, который делает запрос на метод: https://playground.learnqa.ru/api/homework_cookie
Этот метод возвращает какую-то cookie с каким-то значением. Необходимо с помощью функции print() понять что за cookie
и с каким значением, и зафиксировать это поведение с помощью assert
Чтобы pytest не игнорировал print() необходимо использовать ключик "-s": python -m pytest -s my_test.py"""

response = requests.get("https://playground.learnqa.ru/api/homework_cookie")
print(response.cookies)
assert "hw_value" == response.cookies.get("HomeWork")

"""Тест запроса на метод header
Необходимо написать тест, который делает запрос на метод: https://playground.learnqa.ru/api/homework_header
Этот метод возвращает headers с каким-то значением. Необходимо с помощью функции print() понять что за headers
и с каким значением, и зафиксировать это поведение с помощью assert
Чтобы pytest не игнорировал print() необходимо использовать ключик "-s": python -m pytest -s my_test.py"""

response = requests.get("https://playground.learnqa.ru/api/homework_header")
print(response.headers)
assert "Some secret value" == response.headers.get("x-secret-homework-header")

"""User Agent
User Agent - это один из заголовков, позволяющий серверу узнавать, с какого девайса и браузера пришел запрос. 
Он формируется автоматически клиентом, например браузером. 
Определив, с какого девайса или браузера пришел к нам пользователь мы сможем отдать ему только тот контент, который ему нужен.
Наш разработчик написал метод: https://playground.learnqa.ru/ajax/api/user_agent_check
Метод определяет по строке заголовка User Agent следующие параметры:
device - iOS или Android
browser - Chrome, Firefox или другой браузер
platform - мобильное приложение или веб
Если метод не может определить какой-то из параметров, он выставляет значение Unknown.
Наша задача написать параметризированный тест. Этот тест должен брать из дата-провайдера User Agent и ожидаемые значения,
GET-делать запрос с этим User Agent и убеждаться, что результат работы нашего метода правильный - т.е. в ответе ожидаемое значение всех трех полей.
"""
def return_device():
    device = ["iOS", "Android"]
    return random.choice(device)
def return_platform():
    platform = ["Web", "Mobile"]
    return random.choice(platform)
def return_browser():
    browser = ["Chrome", "Safari", "Mozilla", "Opera", "Edge"]
    return random.choice(browser)
def return_user_agent():
    user_agent = [
        "Mozilla/5.0 (Linux; U; Android 4.0.2; en-us; Galaxy Nexus Build/ICL53F) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",
        "Mozilla/5.0 (iPad; CPU OS 13_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/91.0.4472.77 Mobile/15E148 Safari/604.1",
        "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.100.0",
        "Mozilla/5.0 (iPad; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"
    ]
    return random.choice(user_agent)
all_device = []
for i in range(5):
    lst = (return_user_agent(), return_platform(), return_browser(), return_device())
    all_device.append(lst)

@pytest.mark.parametrize("user_agent, platform, browser, device", all_device)
def test_user_agent(user_agent, platform, browser, device):
    response = requests.get(
    "https://playground.learnqa.ru/ajax/api/user_agent_check",
    headers={"User-Agent": user_agent}
    )
    response_dict = response.json()
    assert response_dict["platform"] == platform, f"Unexpected platform value for User-Agent {user_agent}. Got {response_dict['platform']}, expected {platform}"
    assert response_dict["device"] == device, f"Unexpected device value for User-Agent {user_agent}. Got {response_dict['device']}, expected {device}"
    assert response_dict["browser"] == browser, f"Unexpected browser value for User-Agent {user_agent}. Got {response_dict['browser']}, expected {browser}"



# user_agents_data = [
#     ("Mozilla/5.0 (Linux; Android 8.0.0; Pixel 2 Build/OPD3.170816.012) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Mobile Safari/537.36", "Android", "Chrome", "Web"),
#     ("Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/86.0.4240.93 Mobile/15E148 Safari/604.1", "iOS", "Chrome", "Web"),
#     ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299", "Unknown", "Chrome", "Web"),
#     ("Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)", "Unknown", "Unknown", "Web"),
#     ("Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Mobile Safari/537.36", "Android", "Chrome", "Web")
# ]
#
# @pytest.mark.parametrize("user_agent, device, browser, platform", user_agents_data)
# def test_user_agent_check(user_agent, device, browser, platform):
#     response = requests.get(
#         "https://playground.learnqa.ru/ajax/api/user_agent_check",
#         headers={"User-Agent": user_agent}
#     )
#     response_dict = response.json()
#     assert response_dict["platform"] == platform, f"Unexpected platform value for User-Agent {user_agent}. Got {response_dict['platform']}, expected {platform}"
#     assert response_dict["device"] == device, f"Unexpected device value for User-Agent {user_agent}. Got {response_dict['device']}, expected {device}"
#     assert response_dict["browser"] == browser, f"Unexpected browser value for User-Agent {user_agent}. Got {response_dict['browser']}, expected {browser}"


