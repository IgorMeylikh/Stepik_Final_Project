# Импортируем класс BasePage из файла base_page.py
from .base_page import BasePage
# Подключаем библиотеку By для более красивого и универсального кода
from selenium.webdriver.common.by import By
# Подлючаем файл с локаторами
from .locators import MainPageLocators
# Подключаем файл login_page.py для возврата на страницу
from .login_page import LoginPage


# Создаём класс MainPage, который является наследником класса BasePage
class MainPage(BasePage):
    def go_to_login_page(self):
        link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        link.click() 
        alert = self.browser.switch_to.alert
        alert.accept()        
        return LoginPage(browser=self.browser, url=self.browser.current_url) # Возврат на страницу
        

    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"



    