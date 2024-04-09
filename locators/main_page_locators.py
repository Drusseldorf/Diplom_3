from selenium.webdriver.common.by import By


class MainPageLocators:

    PERSONAL_ACCOUNT = By.CSS_SELECTOR, '[href="/account"]'
    INGREDIENTS_BLOCK = By.CSS_SELECTOR, '[class*="BurgerIngredients_ingredients__menuContainer"]'
    CONSTRUCTOR = By.XPATH, '//li/a[@href="/"]'
    ORDERS_FEED = By.CSS_SELECTOR, '[href="/feed"]'
    INGREDIENTS_LIST_ELEMENTS = By.CSS_SELECTOR, '[href*="/ingredient"]'
    MODAL_INGREDIENT_OPENED = By.CSS_SELECTOR, '[class*="Modal_modal_opened"]'
    CLOSE_MODAL = By.CSS_SELECTOR, '[class*="Modal_modal__close"]'
    BURGER_CONSTRUCTOR = By.CSS_SELECTOR, 'ul[class*="BurgerConstructor_basket__list"]'
    COUNTERS_ELEMENTS = By.CSS_SELECTOR, 'p[class*="counter_counter__num"]'
    MAKE_ORDER_BUTTON = By.XPATH, '//button[text()="Оформить заказ"]'
    MODAL_ORDER_NUMBER = By.CSS_SELECTOR, '[class*="Modal_modal__contentBox"]'
