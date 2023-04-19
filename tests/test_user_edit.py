from pages.assertions import Assertion
from pages.base_page import BasePage
from pages.my_requests import MyRequests


class TestUserEdit(BasePage):
    def test_edit_just_created_user(self):
        #REGISTER
        data = self.prepare_registration_date()
        response1 = MyRequests.post("/api/user/", data=data)
        Assertion.assert_code_status(response1, 200)
        Assertion.assert_json_has_key(response1, "id")
        email = data["email"]
        password = data["password"]
        user_id = self.get_json_value(response1, "id")
        #LOGIN
        login_date = {
            "email": email,
            "password": password
        }
        response2 = MyRequests.post("/api/user/login", data=login_date)
        auth_sid = self.get_cookie(response2, "auth_sid")
        token = self.get_header(response2, "x-csrf-token")

        #EDIT
        new_name = "Changed Name"
        response3 = MyRequests.put(f"""/api/user/{user_id}""",
                                 headers={"x-csrf-token": token},
                                 cookies={"auth_sid": auth_sid},
                                 data={"firstName": new_name}
                                 )
        Assertion.assert_code_status(response3, 200)
        #GET
        response4 = MyRequests.get(f"""/api/user/{user_id}""",
                                 headers={"x-csrf-token": token},
                                 cookies={"auth_sid": auth_sid}
                                 )
        Assertion.assert_json_value_by_name(
            response4,
            "firstName",
            new_name,
            "Wrong name of the user after edit"
        )
