import allure

from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage
from helpers.js_scripts import DragAndDrop


class MainPage(BasePage):

    @allure.step('Нажать на Личный кабинет')
    def click_on_personal_account(self):

        self.click_element(MainPageLocators.PERSONAL_ACCOUNT)

    @allure.step('Нажать на Конструктор')
    def click_on_constructor(self):

        self.click_element(MainPageLocators.CONSTRUCTOR)

    @allure.step('Проверить, виден ли блок с ингредиентами')
    def is_ingredients_block_visible(self):

        return self.is_visible(MainPageLocators.INGREDIENTS_BLOCK)

    @allure.step('Нажать на Историю Заказов')
    def click_on_orders_feed(self):

        self.click_element(MainPageLocators.ORDERS_FEED)

    @allure.step('Нажать на первый в списке ингредиент')
    def click_on_first_ingredient(self):

        self.get_list_of_elements(MainPageLocators.INGREDIENTS_LIST_ELEMENTS)[0].click()

    @allure.step('Проверить, открыто ли модальное окно с описание ингредиента')
    def is_modal_ingredient_window_opened(self):

        return self.is_visible(MainPageLocators.MODAL_INGREDIENT_OPENED)

    @allure.step('Нажать на крестик')
    def click_on_close_button(self):

        self.get_list_of_elements(MainPageLocators.CLOSE_MODAL)[0].click()

    @allure.step('Перенести ингредиент в конструктор')
    def drag_and_drop_first_ingredien_to_constructor(self):

        self.drag_and_drop(DragAndDrop.JS_SCRIPT,
                           MainPageLocators.INGREDIENTS_LIST_ELEMENTS,
                           MainPageLocators.BURGER_CONSTRUCTOR)

    @allure.step('Получить значение счетчика ингредиента')
    def get_ingredient_count(self):

        return int(self.get_list_of_elements(MainPageLocators.COUNTERS_ELEMENTS)[0].text)

    @allure.step('Нажать на Оформить заказ')
    def click_make_order_button(self):

        self.click_element(MainPageLocators.MAKE_ORDER_BUTTON)

    @allure.step('Проверить, открыто ли модальное окно с описание заказа')
    def is_modal_order_number_present(self):

        return self.is_visible(MainPageLocators.MODAL_ORDER_NUMBER)
