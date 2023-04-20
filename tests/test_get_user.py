from pages.my_requests import *
from pages.assertions import *
from pages.base_page import *

@allure.epic("Get user")
class TestUserGet(BasePage):
    @allure.description("This method get user detail not auth")
    def test_get_user_detail_not_auth(self):
        response = MyRequests.get("/user/2")
        Assertion.assert_json_has_key(response, "username")
        Assertion.assert_json_has_not_keys(response, ["email", "firstName", "lastName"])
    #
    @allure.description("This method get user details auth as same user")
    def test_get_user_details_auth_as_same_user(self):
        data = {
            "password": "1234",
            "email": "vinkotov@example.com"
        }
        response1 = MyRequests.post("/user/login", data=data)
        auth_sid = self.get_cookie(response1, "auth_sid")
        token = self.get_header(response1, "x-csrf-token")
        user_id_from_auth_method = self.get_json_value(response1, "user_id")

        response2 = MyRequests.get(f"/user/{user_id_from_auth_method}",
                                 headers={"x-csrf-token": token},
                                 cookies={"auth_sid": auth_sid})
        Assertion.assert_json_has_keys(response2, ["username", "email", "firstName", "lastName"])

    @allure.description("This method get user details auth as different user")
    def test_get_user_details_auth_as_different_user(self):
        data = {
            "password": "1234",
            "email": "vinkotov@example.com"
        }
        response1 = MyRequests.post("/user/login", data=data)
        auth_sid = self.get_cookie(response1, "auth_sid")
        token = self.get_header(response1, "x-csrf-token")

        response2 = MyRequests.get("/user/68863",
                                   headers={"x-csrf-token": token},
                                   cookies={"auth_sid": auth_sid})

        Assertion.assert_json_has_key(response2, "username")
        Assertion.assert_json_has_not_keys(response2, ["email", "firstName", "lastName"])

        