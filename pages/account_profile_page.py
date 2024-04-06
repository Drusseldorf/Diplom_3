from locators.account_profile_locators import AccountProfilePageLocators
from pages.base_page import BasePage


class AccountProfilePage(BasePage):

    def is_profile_present(self):

        return self.is_visible(AccountProfilePageLocators.ACCOUNT_PROFILE)

    def open_orders_history(self):

        self.click_element(AccountProfilePageLocators.ORDERS_HISTORY)

    def is_orders_list_present(self):

        return self.is_present_in_dom(AccountProfilePageLocators.ORDERS_LIST)

    def click_on_exit(self):

        self.click_element(AccountProfilePageLocators.EXIT_BUTTON)
