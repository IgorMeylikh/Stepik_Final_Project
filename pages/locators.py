from selenium.webdriver.common.by import By

# Так как это присутствует на каждой странице, то вынесли в локаторы
class BasePageLocators:
    LOGIN_LINK = (By.ID, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_BUTTON = (By.CSS_SELECTOR, "span[class='btn-group'] a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.ID, "register_form")
    EMAIL_FIELD = (By.ID, 'id_registration-email')
    FIRST_PASSWORD_FIELD = (By.ID, 'id_registration-password1')
    SECOND_PASSWORD_FIELD = (By.ID, 'id_registration-password2')
    BUTTON_SEND_REGISTER_FORM = (By.CSS_SELECTOR, 'button[name="registration_submit"]')

class ProductPageLocators:
    # ADD_TO_BASKET_BUTTON = (By.XPATH, "//button[contains(@class, 'btn-add-to-basket')]")
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, 'button[data-loading-text="Adding..."]')
    PRODUCT_NAME = (By.CSS_SELECTOR, "div h1")
    ADD_TO_BASKET_MESSAGE = (By.CSS_SELECTOR, "div.alertinner > strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main p[class='price_color']")
    BASKET_PRICE = (By.CSS_SELECTOR, "div.alert div p strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages div:nth-child(1)")    

class BasketPageLocators:
    MESSAGE_EMPTY_BASKET = (By.CSS_SELECTOR, "#content_inner")
    ITEMS_TO_BUY_NOW = (By.CSS_SELECTOR, ".basket-items")


    