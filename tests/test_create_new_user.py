import random
import allure
from pages.assertions import Assertion
from pages.base_page import BasePage
from pages.my_requests import MyRequests

@allure.epic("Register user")
class TestUserRegister(BasePage):
    @allure.description("This method created user successfully")
    def test_create_user_successfully(self):
        data = self.prepare_registration_date()
        response = MyRequests.post("/user/", data=data)
        Assertion.assert_code_status(response, 200)
        Assertion.assert_json_has_key(response, "id")
        print(response.text)

    @allure.description("This method create user with existing email")
    def test_create_user_with_existing_email(self):
        data = self.prepare_registration_date("vinkotov@example.com")
        response = MyRequests.post("/user/", data=data)
        Assertion.assert_code_status(response, 400)
        assert response.content.decode('utf-8') == "Users with email 'vinkotov@example.com' already exists", f"Unexpected content {response.content.decode('utf-8')}"

    @allure.description("This method create user with wrong email")
    def test_create_user_with_wrong_email(self):
        data = self.prepare_registration_date("vinkotovexample.com")
        response = MyRequests.post("/user/", data=data)
        Assertion.assert_code_status(response, 400)
        assert response.content.decode('utf-8') == "Invalid email format", f"Unexpected content {response.content.decode('utf-8')}"

    @allure.description("This method create user with short username")
    def test_create_user_with_short_user_name(self):
        data = self.prepare_registration_date()
        for key, value in data.items():
            if key == 'username':
                data[key] = random.choice(list(value))
        response = MyRequests.post("/user/", data=data)
        Assertion.assert_code_status(response, 400)
        assert response.content.decode('utf-8') == "The value of 'username' field is too short", f"Unexpected content {response.content.decode('utf-8')}"

    @allure.description("This method create user with empty field")
    def test_create_user_with_empty_field(self):
        data = self.prepare_registration_date()
        lst = random.choice(["username", "firstName", "lastName"])
        data[lst] = ''
        response = MyRequests.post("/user/", data=data)
        Assertion.assert_code_status(response, 400)
        assert response.content.decode('utf-8') == f"The value of '{lst}' field is too short", f"Unexpected content {response.content.decode('utf-8')}"

    @allure.description("This method create user with empty field")
    def test_create_user_with_too_long_name(self):
        data = self.prepare_registration_date()
        long_name = data["firstName"]
        data["firstName"] = long_name*50
        response = MyRequests.post("/user/", data=data)
        Assertion.assert_code_status(response, 400)
        assert response.content.decode('utf-8') == f"The value of 'firstName' field is too long", f"Unexpected content {response.content.decode('utf-8')}"