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
        locator = (By.CSS_SELECTOR, f'[data-test="add-to-cart-sauce-labs-{product_name}"]')
        self.driver.find_element(*locator).click()

    @allure.step("Удаление товара '{product_name}' из корзины")
    def remove_product_from_cart_by_name(self, product_name):
        locator = (By.CSS_SELECTOR, f'[data-test="remove-sauce-labs-{product_name}"]')
        self.driver.find_element(*locator).click()

    @allure.step("Получение количества товаров в корзине (счётчик)")
    def get_cart_badge_text(self):
        return self.driver.find_element(*self.CART_BADGE).text

    @allure.step("Клик по иконке корзины и переход на страницу корзины")
    def click_cart(self):
        self.driver.find_element(*self.CART_LINK).click()
        
        # Локальный импорт прямо перед возвратом объекта:
        from pages.cart_page import CartPage
        return CartPage(self.driver)
