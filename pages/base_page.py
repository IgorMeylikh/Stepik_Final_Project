class BasePage():
    def __intit__(self, browser, url):
        self.browser = browser
        self.url = url
    def open(self):
        self.browser.get(self.url)