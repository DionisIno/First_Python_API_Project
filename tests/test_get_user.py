from pages.my_requests import *
from pages.assertions import *
from pages.base_page import *

class TestUserGer(BasePage):
    def test_get_user_detail_not_auth(self):
        response = MyRequests.get("/api/user/2")
        Assertion.assert_json_has_key(response, "username")
        Assertion.assert_json_has_not_keys(response, ["email", "firstName", "lastName"])

    def test_get_user_details_auth_as_same_user(self):
        data = {
            "password": "1234",
            "email": "vinkotov@example.com"
        }
        response1 = MyRequests.post("/api/user/login", data=data)
        auth_sid = self.get_cookie(response1, "auth_sid")
        token = self.get_header(response1, "x-csrf-token")
        user_id_from_auth_method = self.get_json_value(response1, "user_id")

        response2 = MyRequests.get(f"/api/user/{user_id_from_auth_method}",
                                 headers={"x-csrf-token": token},
                                 cookies={"auth_sid": auth_sid})
        Assertion.assert_json_has_keys(response2, ["username", "email", "firstName", "lastName"])
        