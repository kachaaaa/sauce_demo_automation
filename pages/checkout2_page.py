import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CheckoutTwoPage(BasePage):
    FINISH_BUTTON = (By.ID, "finish")

    @allure.step("Клик по кнопке Finish для завершения заказа")
    def click_finish(self):
        self.click_element(self.FINISH_BUTTON)
