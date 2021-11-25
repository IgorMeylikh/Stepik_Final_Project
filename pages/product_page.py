from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def should_be_add_to_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.BUTTON_ADD_TO_BASKET), "Button add to basket not presented"

    def save_product_name(self):
        return self.get_text_from_element(*ProductPageLocators.PRODUCT_NAME_H1)

    def add_to_basket(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET)
        add_to_basket_button.click()

    def should_be_product_in_basket_message(self, product_name):
        added_product_name = self.get_text_from_element(*ProductPageLocators.ALERT_SUCCESS)
        expected_string = product_name + " has been added to your basket."
        assert expected_string == added_product_name, \
            f"Expected product alert got '{expected_string}' but got '{added_product_name}' "

    def save_product_value(self):
        return self.get_text_from_element(*ProductPageLocators.MAIN_PRODUCT_PRICE)

    def should_be_basket_value(self, product_value):
        basket_value = self.get_text_from_element(*ProductPageLocators.BASKET)
        expected_string = "Basket total: " + product_value + "\nView basket"
        assert expected_string == basket_value, \
            f"Expected basket value got '{expected_string}' but got '{basket_value}' "

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.ALERT_SUCCESS), \
            "Success message is presented, but should not be"

    def should_success_message_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.ALERT_SUCCESS), \
            "Success message should be disappeared, but still present"
