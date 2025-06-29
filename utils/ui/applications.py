
from selenium import webdriver


class InitBrowser:

    @staticmethod
    def init_browser(application_browser):

        if application_browser == "Chrome":
            browser = webdriver.Chrome()
            return browser

        elif application_browser == "Firefox":
            browser = webdriver.Firefox()
            return browser

        elif application_browser == "Edge":
            browser = webdriver.Edge()
            return browser

        elif application_browser == "Ie":
            browser = webdriver.Ie()
            return browser

        else:
            return None

