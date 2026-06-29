import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CartPage(BasePage):
    # Локатор заголовка страницы (на SauceDemo это элемент с текстом "Your Cart")
    TITLE = (By.CSS_SELECTOR, ".title")

    @allure.step("Получение заголовка страницы корзины")
    def get_title_text(self):
        """Возвращает текст заголовка, чтобы убедиться, что мы в корзине"""
        return self.driver.find_element(*self.TITLE).text
