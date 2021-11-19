# Подключаем библиотеку By для более красивого и универсального кода
from selenium.webdriver.common.by import By
# Импортируем класс BasePage из файла base_page.py
from .base_page import BasePage
# Подлючаем файл с локаторами
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def should_be_add_to_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BUTTON), "ADD_TO_BASKET_BUTTON is not presented"    
    
