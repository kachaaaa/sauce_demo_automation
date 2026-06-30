import allure
import pytest

@allure.epic("UI Automation Framework")
@allure.feature("Checkout & Order Placement")
class TestCheckout:

    @allure.story("Successful End-to-End Purchase")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_successful_checkout_information(self, logged_in_inventory_page):
        """Тест проверяет сквозной сценарий заказа от корзины до страницы Finish"""
        inventory_page = logged_in_inventory_page
        driver = inventory_page.driver

        inventory_page.add_product_to_cart_by_name("Sauce Labs Backpack")

        cart_page = inventory_page.click_cart()

        checkout_page = cart_page.click_checkout()

        with allure.step("Заполнение формы персональных данных"):
            checkout_page.enter_first_name("Tony")
            checkout_page.enter_last_name("Stark")
            checkout_page.enter_postal_code("12345")

        checkout2_page = checkout_page.click_continue()

        with allure.step("Проверка успешного перехода на шаг Checkout: Overview"):
            assert "checkout-step-two.html" in driver.current_url, "Не произошло перенаправления на второй шаг чекаута!"

        checkout2_page.click_finish()

        with allure.step("Проверка успешного завершения заказа"):
            assert "checkout-complete.html" in driver.current_url, "Заказ не был успешно завершен!"
            
