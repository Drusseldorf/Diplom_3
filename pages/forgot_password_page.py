from locators.forgot_password_locators import ForgotPasswordPageLocators
from pages.base_page import BasePage
from helpers.generate import Generate


class ForgotPasswordPage(BasePage):

    def reset_button_is_present(self):

        return self.is_visible(ForgotPasswordPageLocators.RESET_PASSWORD)

    def click_reset_password(self):

        return self.click_element(ForgotPasswordPageLocators.RESET_PASSWORD)

    def fill_email(self, email=None):

        if email is None:
            email = Generate.email()

        self.input_text(ForgotPasswordPageLocators.INPUT_EMAIL, email)
