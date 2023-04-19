from pages.assertions import Assertion
from pages.base_page import BasePage
from pages.my_requests import MyRequests


class TestUserRegister(BasePage):
    def test_create_user_successfully(self):
        data = self.prepare_registration_date()
        response = MyRequests.post("/api/user/", data=data)
        Assertion.assert_code_status(response, 200)
        Assertion.assert_json_has_key(response, "id")

    def test_create_user_with_existing_email(self):
        data = self.prepare_registration_date("vinkotov@example.com")
        response = MyRequests.post("/api/user/", data=data)
        Assertion.assert_code_status(response, 400)
        assert response.content.decode('utf-8') == "Users with email 'vinkotov@example.com' already exists", f"Unexpected content {response.content.decode('utf-8')}"