# Импортируем класс ProductPage из файла product_page.py
from .pages.product_page import ProductPage

# Тестирование страницы product. Открываем страницу
def test_guest_open_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)                           # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()  
    page.should_be_add_to_basket_button()

# Тестирование страницы login
# def test_guest_can_go_to_login_page_and_check_login_url(browser):

#     link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
#     page = LoginPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
#     # Нам незачем открывать саму страницу в браузере, чтобы проверить, что в линке есть слово login.
#     # Если нам надо на уже открытой после редиректа странице проверять наличие,
#     # то тогда нам надо сначала текущий URL прочитать и там уже сравнивать    
#     page.open()                      # открываем страницу
#     page.should_be_login_url()       # проверяем URL

# def test_guest_check_login_form(browser):
#     link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
#     page = LoginPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
#     page.open()                      # открываем страницу
#     page.should_be_login_form()      # проверяем наличие #login_form

# def test_guest_check_registration_form(browser):
#     link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
#     page = LoginPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
#     page.open()                      # открываем страницу
#     page.should_be_register_form()   # проверяем наличие #register_form    

