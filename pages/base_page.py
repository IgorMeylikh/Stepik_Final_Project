# Чтобы импортировать нужное нам исключение, в самом верху файла нужно указать: 
from selenium.common.exceptions import NoSuchElementException

class BasePage():
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        # Добавим команлу неявного ожидания
        self.browser.implicitly_wait(timeout)
   
    # конструктор запуска браузера
    def open(self):
        self.browser.get(self.url)

    # реализуем метод is_element_present, в котором будем перехватывать исключение.
    # В него будем передавать два аргумента: как искать (css, id, xpath и тд)
    # и, собственно, что искать (строку-селектор). 
    
    def is_element_present(self, how, what):
        # Чтобы перехватывать исключение, нужна конструкция try/except:
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True