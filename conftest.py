import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser): #парсим язык
    parser.addoption('--language', action='store', default='en',
                    help="Choose language")


@pytest.fixture(scope="session")
def browser(request):
    user_language = request.config.getoption("language")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})

    print("\nstart browser for test..")
    browser = webdriver.Chrome(options=options)

    yield browser
    print("\nquit browser..")
    browser.quit()
 
# Вариант вызова браузера с проверкой введённого яыка
# @pytest.fixture(scope="function")
# def browser(request):
#     languages = "ar ca cs da de el es fi fr it ko nl pl pt pt-br ro ru sk uk zh-hans en-gb zh-cn ko en"
#     language = request.config.getoption("language")
#     if (language + " ") in languages:
#         print("\nStart chrome browser for test..")
#         options = Options()
#         options.add_experimental_option(
#             'prefs', {'intl.accept_languages': language})
#         browser = webdriver.Chrome(options=options)
#     else:
#         print("\nlanguage {} not supported :(\ntry: ar ca cs da de el es fi fr it ko nl pl pt pt-br ro ru sk uk zh-hans en-gb zh-cn ko en".format(language))
#         pytest.fail("Wrong Language")
#         # assert 0
#     yield browser
#     print("\nQuit browser...")
#     browser.quit()


#Альтернативный вариант вызова браузера с проверкой браузера
# @pytest.fixture(scope="function")
# def browser(request):
#     browser_name = request.config.getoption("--browser_name")
#     user_language = request.config.getoption("--language")
#     if browser_name == "chrome":
#         print("\nstart chrome browser for test..")
#         options = Options()

#         options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
#         browser = webdriver.Chrome(options=options)
#     elif browser_name == "firefox":
#         print("\nstart firefox browser for test..")
#         fp = webdriver.FirefoxProfile()

#         fp.set_preference("intl.accept_languages", "{0}".format(user_language))
#         # fp.set_preference("intl.accept_languages", user_language)
#         browser = webdriver.Firefox(firefox_profile=fp)
#     else:
#         raise pytest.UsageError("--browser_name should be chrome or firefox")
#     yield browser
#     print("\nquit browser..")
#     browser.quit()