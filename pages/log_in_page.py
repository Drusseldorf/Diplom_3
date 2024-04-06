from locators.log_in_page_locators import LogInPageLocators
from pages.base_page import BasePage


class LogInPage(BasePage):

    def click_reset_password(self):

        self.click_element(LogInPageLocators.RESET_PASSWORD)

    def fill_creds_and_login(self, email, password):

        self.input_text(LogInPageLocators.INPUT_EMAIL_FIELD, email)
        self.input_text(LogInPageLocators.INPUT_PASSWORD_FIELD, password)
        self.click_element(LogInPageLocators.LOGIN_BUTTON)

    def is_login_button_present(self):

        return self.is_visible(LogInPageLocators.LOGIN_BUTTON)
