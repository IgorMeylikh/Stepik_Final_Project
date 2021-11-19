# Импортируем класс BasePage из файла base_page.py
from .base_page import BasePage
# Подключаем библиотеку By для более красивого и универсального кода
from selenium.webdriver.common.by import By
# Подлючаем файл с локаторами
from .locators import MainPageLocators

# Создаём класс MainPage, который является наследником класса BasePage
class MainPage(BasePage):
    def go_to_login_page(self):
        login_link = self.is_element_present(*MainPageLocators.LOGIN_LINK)
        login_link.click() 

    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"