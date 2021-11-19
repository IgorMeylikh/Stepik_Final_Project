# Подключаем библиотеку By для более красивого и универсального кода
from selenium.webdriver.common.by import By
# Импортируем класс BasePage из файла base_page.py
from .base_page import BasePage
# Подлючаем файл с локаторами
from .locators import LoginPageLocators

class LoginPage(BasePage):
    # def should_be_login_page(self):
    #     self.should_be_login_url()
    #     self.should_be_login_form()
    #     self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        print(self.current_url)
        assert "login" in self.url, "Login is not presented"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        print(self.is_element_present(*LoginPageLocators.LOGIN_FORM))
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        print(self.is_element_present(*LoginPageLocators.LOGIN_REGISTER_FORM))
        assert self.is_element_present(*LoginPageLocators.LOGIN_REGISTER_FORM), "Login register form is not presented"
