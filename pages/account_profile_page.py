import allure

from locators.account_profile_locators import AccountProfilePageLocators
from pages.base_page import BasePage


class AccountProfilePage(BasePage):

    @allure.step('Проверить, что виден пункт "Профиль"')
    def is_profile_present(self):

        return self.is_visible(AccountProfilePageLocators.ACCOUNT_PROFILE)

    @allure.step('Открыть историю заказов')
    def open_orders_history(self):

        self.click_element(AccountProfilePageLocators.ORDERS_HISTORY)

    @allure.step('Проверить, что виден пункт "История заказов"')
    def is_orders_list_present(self):

        return self.is_present_in_dom(AccountProfilePageLocators.ORDERS_LIST)

    @allure.step('Нажать на Выход')
    def click_on_exit(self):

        self.click_element(AccountProfilePageLocators.EXIT_BUTTON)

    @allure.step('Получить номер первого в списке заказа')
    def get_first_order_number(self):

        return self.get_list_of_elements(AccountProfilePageLocators.ACCOUNT_ORDERS_ELEMENTS)[0].text
