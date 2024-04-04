from locators.log_in_page_locators import LogInPageLocators
from pages.base_page import BasePage


class LogInPage(BasePage):

    def click_reset_password(self):

        self.click_element(LogInPageLocators.RESET_PASSWORD)
