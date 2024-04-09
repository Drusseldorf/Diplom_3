import allure

from pages.orders_feed_page import OrdersFeedPage
from pages.account_profile_page import AccountProfilePage
from pages.main_page import MainPage
from data import URL
from http_requests.make_an_order import Order


class TestOrdersFeed:

    @allure.title('Нажатие на номер заказа открывает модальное окно с деталями заказа')
    def test_click_order_open_modal(self, driver):

        orders_feed_page = OrdersFeedPage(driver)
        orders_feed_page.open_page(URL.ORDERS_FEED_PAGE_URL)

        orders_feed_page.click_on_first_order()

        assert orders_feed_page.is_order_details_modal_opened()

    @allure.title('Заказы пользователя отображаются в списке заказов')
    def test_user_orders_present_in_orders_feed(self, driver, authorized_account_user):

        orders_feed_page = OrdersFeedPage(driver)
        account_page = AccountProfilePage(driver)
        main_page = MainPage(driver)

        Order.create(authorized_account_user.accessToken)

        main_page.open_page(URL.MAIN_PAGE_URL)
        main_page.click_on_personal_account()

        account_page.open_orders_history()
        order_number = account_page.get_first_order_number()

        orders_feed_page.open_page(URL.ORDERS_FEED_PAGE_URL)

        orders_feed = orders_feed_page.get_list_order_numbers()

        assert order_number in orders_feed

    @allure.title('Счетчик общего числа заказов увеличивается при создании заказа')
    def test_overall_orders_counter(self, driver, authorized_account_user):

        main_page = MainPage(driver)
        orders_feed_page = OrdersFeedPage(driver)

        main_page.open_page(URL.MAIN_PAGE_URL)
        main_page.click_on_orders_feed()

        number_before = orders_feed_page.get_overall_orders_number()

        Order.create(authorized_account_user.accessToken)

        assert orders_feed_page.is_overall_order_counter_increased(number_before)

    @allure.title('Счетчик заказов за сегодня увеличивается при создании заказа')
    def test_todays_orders_counter(self, driver, authorized_account_user):

        main_page = MainPage(driver)
        orders_feed_page = OrdersFeedPage(driver)

        main_page.open_page(URL.MAIN_PAGE_URL)
        main_page.click_on_orders_feed()

        number_before = orders_feed_page.get_todays_orders_number()

        Order.create(authorized_account_user.accessToken)

        assert orders_feed_page.is_todays_order_counter_increased(number_before)

    @allure.title('При создании заказа, его номер отображается в списке заказов В работе')
    def test_order_in_progress(self, driver, authorized_account_user):

        main_page = MainPage(driver)
        orders_feed_page = OrdersFeedPage(driver)

        main_page.open_page(URL.MAIN_PAGE_URL)
        main_page.click_on_orders_feed()

        order_number = Order.create(authorized_account_user.accessToken).order.number

        assert orders_feed_page.is_order_in_progress(order_number)
