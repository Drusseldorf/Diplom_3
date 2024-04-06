from pages.base_page import BasePage
from locators.reset_password_page_locators import ResetPasswordLocators


class ResetPasswordPage(BasePage):

    def input_code_field_is_present(self):

        return self.is_visible(ResetPasswordLocators.INPUT_CODE)

    def click_on_show_password_button(self):

        self.click_element(ResetPasswordLocators.SHOW_PASSWORD_BUTTON)

    def is_password_field_active(self):

        return self.is_visible(ResetPasswordLocators.FIELD_PASSWORD_HIGHLIGHTED)
