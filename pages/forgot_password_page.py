from locators.forgot_password_locators import ForgotPasswordPageLocators
from pages.base_page import BasePage


class ForgotPasswordPage(BasePage):

    def reset_button_is_present(self):

        return self.is_present(ForgotPasswordPageLocators.RESET_PASSWORD)

    def click_reset_password(self):

        return self.click_element(ForgotPasswordPageLocators.RESET_PASSWORD)
