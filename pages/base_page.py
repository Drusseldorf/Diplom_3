import allure
from selenium.common import TimeoutException
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

    def is_visible(self, locator):

        result = True

        try:
            wait(self.driver, timeout=3).until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            result = False

        return result

    def is_present_in_dom(self, locator):

        result = True

        try:
            wait(self.driver, timeout=3).until(EC.presence_of_element_located(locator))
        except TimeoutException:
            result = False

        return result

    def get_list_of_elements(self, locator):

        return wait(self.driver, timeout=3).until(EC.presence_of_all_elements_located(locator))

    def drag_and_drop(self, js_scripts, locator, target_locator):

        element = wait(self.driver, timeout=3).until(EC.presence_of_all_elements_located(locator))[0]
        target_element = self.driver.find_element(*target_locator)
        self.driver.execute_script(js_scripts, element, target_element)
