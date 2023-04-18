import json.decoder
from requests import *


class BasePage:
    def get_cookie(self, response: Response, cookie_name):
        assert cookie_name in response.cookies, f"""Cannot find cookie with name {cookie_name} in the response"""
        return response.cookies[cookie_name]

    def get_header(self, response: Response, headers_name):
        assert headers_name in response.headers, f"""Cannot find header with name {headers_name} in the response"""
        return response.headers[headers_name]

    def get_json_value(self, response: Response, name):
        try:
            response_json = response.json()
        except json.decoder.JSONDecodeError:
            assert False, f"""response is not in JSON format. Response text is {response.text}"""
        assert name in response_json, f"""Response JSON doesn't have key '{name}'"""
        return response_json[name]