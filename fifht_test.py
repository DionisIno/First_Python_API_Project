import requests
import pytest

class TestUserAuth:

    def test_auth_user(self):
        data = {
            "email": "vinkotov@example.com",
            "password": "1234"
        }
        response1 = requests.post("https://playground.learnqa.ru/api/user/login", data=data)
        assert "auth_sid" in response1.cookies, "There is not auth_sid in the cookies"
        assert "x-csrf-token" in response1.headers, "There is not x-csrf-token in the headers"
        assert "user_id" in response1.json(), "there is not user_id in yhe response"

        auth_sid = response1.cookies.get("auth_sid")
        token = response1.headers.get("x-csrf-token")
        user_id = response1.json()["user_id"]

        response2 = requests.get(
            "https://playground.learnqa.ru/api/user/auth",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid},
        )
        assert 'user_id' in response2.json(), "There is not user id in the second response"
        assert user_id == response2.json()['user_id'], "There is not user id equal response id"