from selenium.webdriver import Keys
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def open_page(self, url):
        self.driver.get(url)

    def get_element_text(self, locator):
        return wait(self.driver, timeout=3).until(EC.presence_of_element_located(locator)).text

    def click_element(self, locator):
        wait(self.driver, timeout=3).until(EC.element_to_be_clickable(locator)).click()

    def input_text(self, locator, text):
        self.driver.find_element(*locator).send_keys(text)

    def press_enter(self, locator):
        self.driver.find_element(*locator).send_keys(Keys.ENTER)

    def is_page_opened(self, url):
        wait(self.driver, 10).until(EC.url_to_be(url))
        return url == self.driver.current_url

    def switch_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[1])

    def is_present(self, locator):
        element = wait(self.driver, timeout=3).until(EC.visibility_of_element_located(locator))
        return element.is_displayed()
