from pages.log_in_page import LogInPage
from pages.forgot_password_page import ForgotPasswordPage
from data import URL


class TestOpenResetPasswordPage:

    def test_open_reset_password_page(self, driver):

        log_in_page = LogInPage(driver)
        log_in_page.open_page(URL.LOG_IN_PAGE_URL)

        log_in_page.click_reset_password()

        forgot_page = ForgotPasswordPage(driver)

        assert forgot_page.reset_button_is_present()
