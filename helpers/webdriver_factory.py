from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager


class WebDriverFactory:
    @staticmethod
    def get_web_driver(browser_name):
        drivers = {
            'firefox': FirefoxWebDriver,
            'chrome': ChromeWebDriver
        }
        driver_class = drivers.get(browser_name)
        if driver_class:
            return driver_class.create_driver()
        else:
            raise ValueError('Invalid browser name. Available options: firefox, chrome')


class FirefoxWebDriver:
    @staticmethod
    def create_driver():
        return webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))


class ChromeWebDriver:
    @staticmethod
    def create_driver():
        return webdriver.Chrome(service=Service(ChromeDriverManager().install()))
