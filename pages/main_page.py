# Импортируем класс BasePage из файла base_page.py
from .base_page import BasePage
# Подключаем библиотеку By для более красивого и универсального кода
from selenium.webdriver.common.by import By

# Создаём класс MainPage, который является наследником класса BasePage
class MainPage(BasePage):
    def go_to_login_page(self):
        login_link = self.browser.find_element(By.CSS_SELECTOR, "#login_link")
        login_link.click() 