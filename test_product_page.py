import time
import pytest
from .pages.base_page import BasePage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
from .pages.main_page import MainPage
from .pages.product_page import ProductPage

# Тестирование страницы product. Открываем страницу
# pytest -v -s --tb=line --language=en test_product_page.py

# product_base_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
# urls = [f"{product_base_link}/?promo=offer{no}" for no in range(10)]
# @pytest.mark.parametrize('link', urls)
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
                                               "/?promo=offer7", marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser, link):
    # в задаче без параметризации заменить link на 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    # и убрать link из аргумента
    page = ProductPage(browser, link)
    # url адрес
    page.open()  # открываем страницу
    page.should_be_add_to_basket_button()  # проверяем что присутсвует кнопка для добавления в корзину
    product_name = page.save_product_name()  # сохраняем наименование продукта
    product_value = page.save_product_value()  # сохраняем цену продукта
    page.add_to_basket()  # добавляем товар в корзину
    page.solve_quiz_and_get_code()  # решаем задачку
    page.should_be_product_in_basket_message(product_name)  # проверяем что присутствует сообщение о том что
    # нужный товар добавлен в корзину
    page.should_be_basket_value(product_value)  # проверяем стоимость товаров в корзине

@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и
    # url адрес
    page.open()  # открываем страницу
    page.should_be_add_to_basket_button()  # проверяем что присутсвует кнопка для добавления в корзину
    page.add_to_basket()  # добавляем товар в корзину
    page.should_not_be_success_message()  # проверяем что нет сообщения о добавлении товара в корзину

def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и
    # url адрес
    page.open()  # открываем страницу
    page.should_not_be_success_message()  # проверяем что нет сообщения о добавлении товара в корзину

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и
    # url адрес
    page.open()  # открываем страницу
    page.should_be_add_to_basket_button()  # проверяем что присутсвует кнопка для добавления в корзину
    page.add_to_basket()  # добавляем товар в корзину
    page.should_success_message_disappeared()  # проверяем что сообщения о добавлении товара в корзину исчезло

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()

@pytest.mark.tasks
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        login_page = LoginPage(browser, link)
        login_page.open()
        email = str(time.time()) + "@fakemail.org"
        login_page.register_new_user(email, "Qw123456789")
        base_page = BasePage(browser, browser.current_url)
        base_page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и
        # url адрес
        page.open()  # открываем страницу
        page.should_not_be_success_message()  # проверяем что нет сообщения о добавлении товара в корзину

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр
        # драйвера и url адрес
        page.open()  # открываем страницу
        page.should_be_add_to_basket_button()  # проверяем что присутсвует кнопка для добавления в корзину
        product_name = page.save_product_name()  # сохраняем наименование продукта
        product_value = page.save_product_value()  # сохраняем цену продукта
        page.add_to_basket()  # добавляем товар в корзину
        page.should_be_product_in_basket_message(product_name)  # проверяем что присутствует сообщение о том что
        # нужный товар добавлен в корзину
        page.should_be_basket_value(product_value)  # проверяем стоимость товаров в корзине

    @pytest.mark.need_review
    def test_guest_cant_see_product_in_basket_opened_from_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"
        page = MainPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url
        # адрес
        page.open()  # открываем страницу
        page.go_to_basket()  # переходим по кнопке в корзину
        basket_page = BasketPage(browser, browser.current_url)
        basket_page.should_not_be_products_in_basket()  # Ожидаем, что в корзине нет товаров
        basket_page.should_basket_empty_text_present()  # Ожидаем, что есть текст о том что корзина пуста
