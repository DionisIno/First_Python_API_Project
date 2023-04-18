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