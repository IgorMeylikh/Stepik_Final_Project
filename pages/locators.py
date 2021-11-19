from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_URL = (By.CSS_SELECTOR, "#login_url")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    LOGIN_REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    ADD_TO_BASKET_FORM = (By.CSS_SELECTOR, '#add_to_basket_form')
    # ADD_TO_BASKET_BUTTON = (ADD_TO_BASKET_FORM.find_element(By.CSS_SELECTOR, 'button[type="submit"]'))
