# Подключаем библиотеку By для более красивого и универсального кода
from selenium.webdriver.common.by import By
# Импортируем класс BasePage из файла base_page.py
from .base_page import BasePage
# Подлючаем файл с локаторами
from .locators import ProductPageLocators
import time

class ProductPage(BasePage):
    def should_be_add_to_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BUTTON), "ADD_TO_BASKET_BUTTON is not presented"   

    def should_be_click_to_button_add_to_basket(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON).click()
        
    def should_be_switch_to_alert(self):
        alert = self.browser.switch_to.alert
        print(alert.text)
        alert.send_keys('Alex')
        time.sleep(1)
        alert.dismiss()
        time.sleep(1)
