from .base_page import BasePage
from .locators import LoginPageLocators
from .locators import BasePageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_LINK), "Login link is not presented"
        assert "login" in self.browser.current_url

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self, email, password):
        login_link = self.browser.find_element(*BasePageLocators.LOGIN_REGISTER_LINK)
        login_link.click()
        input_email = self.browser.find_element(*LoginPageLocators.INPUT_FIELD_EMAIL)
        input_email.send_keys(email)
        input_password1 = self.browser.find_element(*LoginPageLocators.INPUT_FIELD_PASSWORD1)
        input_password1.send_keys(password)
        input_password2 = self.browser.find_element(*LoginPageLocators.INPUT_FIELD_PASSWORD2)
        input_password2.send_keys(password)
        register_button = self.browser.find_element(*LoginPageLocators.BUTTON_REGISTRATION_SUBMIT)
        register_button.click()