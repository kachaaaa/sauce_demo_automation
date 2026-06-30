import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class InventoryPage(BasePage):
    TITLE = (By.CSS_SELECTOR, ".title")
    CART_BADGE = (By.CSS_SELECTOR, ".shopping_cart_badge")
    CART_LINK = (By.CSS_SELECTOR, ".shopping_cart_link")

    @allure.step("Получение заголовка страницы каталога")
    def get_title_text(self):
        return self.driver.find_element(*self.TITLE).text

    @allure.step("Добавление товара '{product_name}' в корзину")
    def add_product_to_cart_by_name(self, product_name):
        formatted_name = product_name.lower().replace(" ", "-")
        if "sauce-labs-" not in formatted_name:
            formatted_name = f"sauce-labs-{formatted_name}"
        locator = (By.CSS_SELECTOR, f'[data-test="add-to-cart-{formatted_name}"]')
        self.click_element(locator)

    @allure.step("Удаление товара '{product_name}' из корзины")
    def remove_product_from_cart_by_name(self, product_name):
        formatted_name = product_name.lower().replace(" ", "-")
        if "sauce-labs-" not in formatted_name:
            formatted_name = f"sauce-labs-{formatted_name}"
        locator = (By.CSS_SELECTOR, f'[data-test="remove-{formatted_name}"]')
        self.click_element(locator)

    @allure.step("Получение количества товаров в корзине (счётчик)")
    def get_cart_badge_text(self):
        from selenium.common.exceptions import TimeoutException
        
        try:
            
            from selenium.webdriver.support.ui import WebDriverWait
            from selenium.webdriver.support import expected_conditions as EC
            
            element = WebDriverWait(self.driver, 2).until(
                EC.presence_of_element_located(self.CART_BADGE)
            )
            return element.text
        except TimeoutException:
            
            return "0"

    @allure.step("Клик по иконке корзины и переход на страницу корзины")
    def click_cart(self):
        self.driver.find_element(*self.CART_LINK).click()
        
        # Локальный импорт прямо перед возвратом объекта:
        from pages.cart_page import CartPage
        return CartPage(self.driver)
