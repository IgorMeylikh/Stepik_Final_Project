from .base_page import BasePage

from .locators import BasketPageLocators

class BasketPage(BasePage):
    def should_not_be_products_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS_BLOCK), \
            "Items is basket presents, but should not be"

    def should_basket_empty_text_present(self):
        basket_text = self.get_text_from_element(*BasketPageLocators.BASKET_TEXT)
        assert basket_text == "Your basket is empty. Continue shopping", "Text about basket empty not presents"