# Подключаем библиотеку By для более красивого и универсального кода
from selenium.webdriver.common.by import By
# Импортируем класс BasePage из файла base_page.py
from .base_page import BasePage
# Подлючаем файл с локаторами
from .locators import LoginPageLocators
import time

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert "login" in self.browser.current_url, "Login is not presented"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        print(self.is_element_present(*LoginPageLocators.LOGIN_FORM))

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        print(self.is_element_present(*LoginPageLocators.REGISTER_FORM))
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Login register form is not presented"

    def register_new_user(self, new_user_email, new_user_password):
        self.browser.find_element(*LoginPageLocators.EMAIL_FIELD).send_keys(new_user_email)
        self.browser.find_element(*LoginPageLocators.FIRST_PASSWORD_FIELD).send_keys(new_user_password)
        self.browser.find_element(*LoginPageLocators.SECOND_PASSWORD_FIELD).send_keys(new_user_password)
        self.browser.find_element(*LoginPageLocators.BUTTON_SEND_REGISTER_FORM).click()
         
