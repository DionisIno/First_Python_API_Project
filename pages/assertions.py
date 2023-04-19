from requests import *
import json

class Assertion:
    @staticmethod
    def assert_json_value_by_name(response: Response, name, expected_value, error_message):
        try:
            response_json = response.json()
        except json.JSONDecodeError:
            assert False, f"""Response is not JSON format. Response text is '{response.text}'"""
        assert name in response_json, f"""response JSON doesn't have key '{name}'"""
        assert response_json[name] == expected_value, error_message

    @staticmethod
    def assert_json_has_key(response: Response, name):
        try:
            response_json = response.json()
        except json.JSONDecodeError:
            assert False, f"""Response is not JSON format. Response text is '{response.text}'"""
        assert name in response_json, f"""response JSON doesn't have key '{name}'"""

    @staticmethod
    def assert_json_has_keys(response: Response, names: list):
        try:
            response_json = response.json()
        except json.JSONDecodeError:
            assert False, f"""Response is not JSON format. Response text is '{response.text}'"""
        for name in names:
            assert name in response_json, f"""response JSON doesn't have key '{name}'"""

    @staticmethod
    def assert_code_status(response: Response, expected_status_code):
        assert response.status_code == expected_status_code, \
            f"""Unexpected status code. Expected: {expected_status_code}. Actual: {response.status_code}"""

    @staticmethod
    def assert_json_has_not_key(response: Response, name):
        try:
            response_json = response.json()
        except json.JSONDecodeError:
            assert False, f"""Response is not JSON format. Response text is '{response.text}'"""
        assert name not in response_json, f"""response JSON shouldn't have key '{name}', but it's present"""

    @staticmethod
    def assert_json_has_not_keys(response: Response, names: list):
        try:
            response_json = response.json()
        except json.JSONDecodeError:
            assert False, f"""Response is not JSON format. Response text is '{response.text}'"""
        for name in names:
            assert name not in response_json, f"""response JSON shouldn't have key '{name}', but it's present"""
