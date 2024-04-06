from selenium.webdriver.common.by import By


class ForgotPasswordPageLocators:

    RESET_PASSWORD = By.XPATH, '//button[text()="Восстановить"]'
    INPUT_EMAIL = By.CSS_SELECTOR, 'input[name="name"]'
