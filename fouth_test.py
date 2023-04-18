import requests
import pytest


class TestFirstAPI:
    names = [
        ("Denis"),
        ("Arsen"),
        ("")
    ]

    @pytest.mark.parametrize('name', names)
    def test_hello_call(self, name):
        url = "https://playground.learnqa.ru/api/hello"
        payload = {"name": name}
        response = requests.get(url, params=payload)
        assert response.status_code == 200, "Wrong response code"
        if len(name) != 0:
            expected_result = f"Hello, {name}"
        else:
            expected_result = "Hello, someone"
        result = response.json()['answer']
        assert result == expected_result

