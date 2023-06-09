import requests
import pytest

class TestUserAuth:
    exclude_params = [
        ("no_cookies"),
        ("no_token")
    ]
    def setup(self):
        data = {
            "email": "vinkotov@example.com",
            "password": "1234"
        }
        response1 = requests.post("https://playground.learnqa.ru/api/user/login", data=data)
        assert "auth_sid" in response1.cookies, "There is not auth_sid in the cookies"
        assert "x-csrf-token" in response1.headers, "There is not x-csrf-token in the headers"
        assert "user_id" in response1.json(), "there is not user_id in yhe response"

        self.auth_sid = response1.cookies.get("auth_sid")
        self.token = response1.headers.get("x-csrf-token")
        self.user_id = response1.json()["user_id"]

    def test_auth_user(self):
        response2 = requests.get(
            "https://playground.learnqa.ru/api/user/auth",
            headers={"x-csrf-token": self.token},
            cookies={"auth_sid": self.auth_sid},
        )
        assert 'user_id' in response2.json(), "There is not user id in the second response"
        assert self.user_id == response2.json()['user_id'], "There is not user id equal response id"

    @pytest.mark.parametrize('condition', exclude_params)
    def test_negative_auth_check(self, condition):
        if condition == "no_cookies":
            response2 = requests.get(
                "https://playground.learnqa.ru/api/user/auth)",
                headers={"x-csrf-token": self.token},
            )
        else:
            response2 = requests.get(
                "https://playground.learnqa.ru/api/user/auth)",
                cookies={"auth_sid": self.auth_sid},
            )
        user_id_from_check_method = response2.text
        assert "This is 404 error" in user_id_from_check_method, f"User is autorized with condition {condition}"