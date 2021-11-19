# Импортируем класс MainPage из файла main_page.py
from .pages.main_page import MainPage
# Импортируем класс LoginPage из файла login_page.py
from .pages.login_page import LoginPage

# Тестирование страницы main
def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com"
    page = MainPage(browser, link)                              # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                                                 # открываем страницу
    login_page = page.go_to_login_page().should_be_login_page() # выполняем метод страницы — переходим на страницу логина

def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
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

