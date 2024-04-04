from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):

    def click_on_personal_account(self):

        self.click_element(MainPageLocators.PERSONAL_ACCOUNT)
