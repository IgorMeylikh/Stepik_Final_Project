from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_BUTTON = (By.CSS_SELECTOR, ".basket-mini a.btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    LOGIN_REGISTER_LINK = (By.ID, "login_link")

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_form")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_link")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    INPUT_FIELD_EMAIL = (By.ID, "id_registration-email")
    INPUT_FIELD_PASSWORD1 = (By.ID, "id_registration-password1")
    INPUT_FIELD_PASSWORD2 = (By.ID, "id_registration-password2")
    BUTTON_REGISTRATION_SUBMIT = (By.NAME, "registration_submit")

class ProductPageLocators():
    BUTTON_ADD_TO_BASKET = (By.CLASS_NAME, "btn-add-to-basket")
    PRODUCT_NAME_H1 = (By.CSS_SELECTOR, ".product_main h1")
    ALERT_SUCCESS = (By.CLASS_NAME, "alertinner")
    MAIN_PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    BASKET = (By.CLASS_NAME, "basket-mini")

class BasketPageLocators():
    BASKET_ITEMS_BLOCK = (By.CLASS_NAME, "basket-items")
    BASKET_TEXT = (By.CSS_SELECTOR, "#content_inner p")