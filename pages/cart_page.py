import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CartPage(BasePage):
    
    TITLE = (By.CSS_SELECTOR, ".title")
    CHECKOUT_BUTTON = (By.ID, "checkout")

    @allure.step("Получение заголовка страницы корзины")
    def get_title_text(self):
        """Возвращает текст заголовка, чтобы убедиться, что мы в корзине"""
        return self.driver.find_element(*self.TITLE).text

    @allure.step("Клик по кнопке Checkout")
    def click_checkout(self):
        """Клик по кнопке Checkout для перехода к оформлению заказа"""
        self.click_element(self.CHECKOUT_BUTTON)
        
        from pages.checkout_page import CheckoutPage
        return CheckoutPage(self.driver)
