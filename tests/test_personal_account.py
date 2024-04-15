import allure

from pages.account_profile_page import AccountProfilePage
from pages.main_page import MainPage
from pages.log_in_page import LogInPage


class TestPersonalAccount:

    @allure.title('Открытие личного кабинета авторизованным пользователем')
    def test_open_personal_account(self, driver, authorized_account_user):

        main_page = MainPage(driver)
        account_profile_page = AccountProfilePage(driver)

        main_page.click_on_personal_account()

        assert account_profile_page.is_profile_present()

    @allure.title('Открытие истории заказов авторизованным пользователем')
    def test_navigate_to_order_history(self, driver, authorized_account_user):

        main_page = MainPage(driver)
        account_profile_page = AccountProfilePage(driver)

        main_page.click_on_personal_account()

        account_profile_page.open_orders_history()

        assert account_profile_page.is_orders_list_present()

    @allure.title('Авторизованный пользователь разлогинивается')
    def test_exit_button(self, driver, authorized_account_user):

        main_page = MainPage(driver)
        account_profile_page = AccountProfilePage(driver)
        login_page = LogInPage(driver)

        main_page.click_on_personal_account()

        account_profile_page.click_on_exit()

        assert login_page.is_login_button_present()
