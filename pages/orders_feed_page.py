import allure
from selenium.common import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators.order_feed_page_locators import OrderFeedListLocators
from pages.base_page import BasePage


class OrdersFeedPage(BasePage):

    @allure.step('Проверить, виден ли список заказов')
    def is_orders_feed_list_visible(self):

        return self.is_present_in_dom(OrderFeedListLocators.ORDERS_FEED_LIST)

    @allure.step('Нажать на первый в списке заказ')
    def click_on_first_order(self):

        self.get_list_of_elements(OrderFeedListLocators.ORDERS_ELEMENTS)[0].click()

    @allure.step('Проверить, открыто ли модальное окно с описание заказа')
    def is_order_details_modal_opened(self):

        return self.is_present_in_dom(OrderFeedListLocators.ORDER_DETAILS_MODAL_OPENED)

    @allure.step('Получение списка номеров заказов')
    def get_list_order_numbers(self):

        order_numbers_elements = self.get_list_of_elements(OrderFeedListLocators.ORDER_NUMBERS_ELEMENTS)

        order_numbers = [order_element.text for order_element in order_numbers_elements]

        return order_numbers

    @allure.step('Получение общего числа заказов')
    def get_overall_orders_number(self):

        return int(self.get_element_text(OrderFeedListLocators.OVERALL_ORDERS_NUMBER))

    @allure.step('Получение числа заказов за сегодня')
    def get_todays_orders_number(self):

        return int(self.get_element_text(OrderFeedListLocators.TODAYS_ORDERS_NUMBER))

    @allure.step('Проверить, увеличилось ли общее число заказов')
    def is_overall_order_counter_increased(self, before_order: int):

        result = True

        try:
            WebDriverWait(self.driver, 10).until(
                EC.text_to_be_present_in_element(OrderFeedListLocators.OVERALL_ORDERS_NUMBER, str(before_order + 1))
            )
        except TimeoutException:

            result = False

        return result

    @allure.step('Проверить, увеличилось ли число заказов за сегодня')
    def is_todays_order_counter_increased(self, before_order: int):

        result = True

        try:
            WebDriverWait(self.driver, 20).until(
                EC.text_to_be_present_in_element(OrderFeedListLocators.TODAYS_ORDERS_NUMBER, str(before_order + 1))
            )
        except TimeoutException:

            result = False

        return result

    @allure.step('Проверить, что номер заказа находится в списке заказов в работе')
    def is_order_in_progress(self, order_number):

        result = True

        try:
            WebDriverWait(self.driver, 20).until(
                EC.text_to_be_present_in_element(OrderFeedListLocators.ORDERS_IN_PROGRESS, str(order_number))
            )
        except TimeoutException:

            result = False

        return result
