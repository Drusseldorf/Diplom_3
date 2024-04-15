from selenium.webdriver.common.by import By


class ResetPasswordLocators:

    INPUT_CODE = By.XPATH, '//label[text()="Введите код из письма"]'
    SHOW_PASSWORD_BUTTON = By.CSS_SELECTOR, '.input__icon-action > svg[xmlns="http://www.w3.org/2000/svg"]'
    FIELD_PASSWORD_HIGHLIGHTED = By.CSS_SELECTOR, '.input_status_active'
