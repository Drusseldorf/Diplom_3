import allure

from pages.base_page import BasePage
from locators.reset_password_page_locators import ResetPasswordLocators


class ResetPasswordPage(BasePage):

    @allure.step('Проверить, что поле ввода пароля из письма имеется на странице')
    def input_code_field_is_present(self):

        return self.is_visible(ResetPasswordLocators.INPUT_CODE)

    @allure.step('Нажать на кнопку показа или скрытия пароля')
    def click_on_show_password_button(self):

        self.click_element(ResetPasswordLocators.SHOW_PASSWORD_BUTTON)

    @allure.step('Проверить, что поле ввода пароля активно')
    def is_password_field_active(self):

        return self.is_visible(ResetPasswordLocators.FIELD_PASSWORD_HIGHLIGHTED)
