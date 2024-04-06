import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

from helpers.generate import Generate
from http_requests.user import User
from data import URL


@pytest.fixture(scope='function')
def driver():

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.set_window_size(1920, 1080)

    yield driver

    driver.quit()


@pytest.fixture(scope='function')
def authorized_account_user(driver):

    response = User.register(**Generate.full_creds())
    access_token = response.accessToken
    refresh_token = response.refreshToken

    driver.get(URL.MAIN_PAGE_URL)

    driver.execute_script(f"localStorage.setItem('accessToken', '{access_token}')")
    driver.execute_script(f"localStorage.setItem('refreshToken', '{refresh_token}')")

    yield response

    if access_token:
        User.delete(access_token)
