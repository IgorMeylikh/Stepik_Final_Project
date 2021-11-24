# Импортируем класс MainPage из файла main_page.py
from .pages.main_page import MainPage
# Импортируем класс LoginPage из файла login_page.py
from .pages.login_page import LoginPage
# Импортируем класс ProductPage из файла product_page.py
from .pages.product_page import ProductPage
# Импортируем класс BasketPage из файла basket_page.py
from .pages.basket_page import BasketPage

import pytest
@pytest.mark.login_guest
class TestLoginFromMainPage(MainPage):
    # не забываем передать первым аргументом self

    def test_guest_can_go_to_login_page(self, browser):
        self.link = "http://selenium1py.pythonanywhere.com"
        page = MainPage(browser, self.link)                              # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()                                                 # открываем страницу
        self.login_page = page.go_to_login_page() # выполняем метод страницы — переходим на страницу логина
        self.login_page = page.should_be_login_link()

    def test_guest_should_see_login_link(self, browser):
        self.link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, self.link)
        page.open()
        page.should_be_login_link()

# Тестирование страницы login
def test_guest_can_go_to_login_page_and_check_login_url(browser):

    link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
    page = LoginPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    # Нам незачем открывать саму страницу в браузере, чтобы проверить, что в линке есть слово login.
    # Если нам надо на уже открытой после редиректа странице проверять наличие,
    # то тогда нам надо сначала текущий URL прочитать и там уже сравнивать    
    page.open()                      # открываем страницу
    page.should_be_login_url()       # проверяем URL

def test_guest_check_login_form(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
    page = LoginPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                      # открываем страницу
    page.should_be_login_form()      # проверяем наличие #login_form

def test_guest_check_registration_form(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
    page = LoginPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                      # открываем страницу
    page.should_be_register_form()   # проверяем наличие #register_form    

def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_empty_basket()
    basket_page.should_be_message_empty_basket()