import pytest

from helpers.generate import Generate
from helpers.webdriver_factory import WebDriverFactory
from http_requests.user import User
from http_requests.models.user_model import RegisterUser
from data import URL


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Browser name: chrome or firefox")


@pytest.fixture(scope='function')
def driver(request):

    browser_name = request.config.getoption('--browser')
    driver_factory = WebDriverFactory()
    driver = driver_factory.get_web_driver(browser_name)
    driver.set_window_size(1920, 1080)

    yield driver

    driver.quit()


@pytest.fixture(scope='function')
def authorized_account_user(driver) -> RegisterUser:

    driver.get(URL.MAIN_PAGE_URL)

    response = User.register(**Generate.full_creds())
    access_token = response.accessToken
    refresh_token = response.refreshToken

    driver.execute_script(f"localStorage.setItem('accessToken', '{access_token}')")
    driver.execute_script(f"localStorage.setItem('refreshToken', '{refresh_token}')")

    yield response

    if access_token:
        User.delete(access_token)
