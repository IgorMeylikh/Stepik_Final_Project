# Импортируем класс BasePage из файла base_page.py
from .base_page import BasePage
# Подключаем библиотеку By для более красивого и универсального кода
from selenium.webdriver.common.by import By


# Создаём класс MainPage, который является наследником класса BasePage
class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)
        



    