import allure

from pages.log_in_page import LogInPage
from pages.forgot_password_page import ForgotPasswordPage
from pages.reset_password_page import ResetPasswordPage
from data import URL


class TestForgotPasswordPage:

    @allure.title('Открытие страницы восстановления пароля')
    def test_open_forgot_password_page(self, driver):

        log_in_page = LogInPage(driver)
        forgot_password_page = ForgotPasswordPage(driver)

        log_in_page.open_page(URL.LOG_IN_PAGE_URL)
        log_in_page.click_reset_password()

        assert forgot_password_page.reset_button_is_present()

    @allure.title('Заполнение поля email')
    def test_fill_email_click_reset(self, driver):

        forgot_password_page = ForgotPasswordPage(driver)
        reset_password_page = ResetPasswordPage(driver)

        forgot_password_page.open_page(URL.FORGOT_PASSWORD_PAGE_URL)
        forgot_password_page.fill_email()
        forgot_password_page.click_reset_password()

        assert reset_password_page.input_code_field_is_present()

    @allure.title('Поле пароля становится активным при нажатии Показать пароль')
    def test_password_visibility_button(self, driver):

        forgot_password_page = ForgotPasswordPage(driver)
        reset_password_page = ResetPasswordPage(driver)

        forgot_password_page.open_page(URL.FORGOT_PASSWORD_PAGE_URL)
        forgot_password_page.fill_email()
        forgot_password_page.click_reset_password()

        reset_password_page.click_on_show_password_button()

        assert reset_password_page.is_password_field_active()
