import allure

from locators.log_in_page_locators import LogInPageLocators
from pages.base_page import BasePage


class LogInPage(BasePage):

    @allure.step('Нажать восстановить пароль')
    def click_reset_password(self):

        self.click_element(LogInPageLocators.RESET_PASSWORD)

    @allure.step('Проверить, что имеется кнопка Войти')
    def is_login_button_present(self):

        return self.is_visible(LogInPageLocators.LOGIN_BUTTON)
