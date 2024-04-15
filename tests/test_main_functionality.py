import allure

from pages.main_page import MainPage
from pages.orders_feed_page import OrdersFeedPage
from data import URL


class TestMainFunctionality:

    @allure.title('Переход в конструктор')
    def test_navigate_to_constructor(self, driver):

        main_page = MainPage(driver)
        main_page.open_page(URL.MAIN_PAGE_URL)

        main_page.click_on_constructor()

        assert main_page.is_ingredients_block_visible()

    @allure.title('Переход в историю заказов')
    def test_navigate_to_orders_feed(self, driver):

        main_page = MainPage(driver)
        orders_feed_page = OrdersFeedPage(driver)
        main_page.open_page(URL.MAIN_PAGE_URL)

        main_page.click_on_orders_feed()

        assert orders_feed_page.is_orders_feed_list_visible()

    @allure.title('Открытие описания ингредиента')
    def test_click_on_ingredien_modal_opened(self, driver):

        main_page = MainPage(driver)
        main_page.open_page(URL.MAIN_PAGE_URL)

        main_page.click_on_first_ingredient()

        assert main_page.is_modal_ingredient_window_opened()

    @allure.title('Нажатие на крестик на модалке ингредиента')
    def test_click_on_close_button(self, driver):

        main_page = MainPage(driver)
        main_page.open_page(URL.MAIN_PAGE_URL)

        main_page.click_on_first_ingredient()

        main_page.click_on_close_button()

        assert not main_page.is_modal_ingredient_window_opened()

    @allure.title('Счетчик ингредиента увеличивается после его добавления в конструктор')
    def test_counter_after_ingredient_added(self, driver):

        main_page = MainPage(driver)
        main_page.open_page(URL.MAIN_PAGE_URL)

        main_page.drag_and_drop_first_ingredien_to_constructor()

        assert main_page.get_ingredient_count() == 2

    @allure.title('Авторизованный пользователь имеет возможность создать заказ')
    def test_authenticated_user_can_make_order(self, driver, authorized_account_user):

        main_page = MainPage(driver)
        main_page.open_page(URL.MAIN_PAGE_URL)

        main_page.drag_and_drop_first_ingredien_to_constructor()

        main_page.click_make_order_button()

        assert main_page.is_modal_order_number_present()
