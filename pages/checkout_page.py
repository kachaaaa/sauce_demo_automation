    
import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.checkout2_page import CheckoutTwoPage

class CheckoutPage(BasePage):
    
    FIRST_NAME_INPUT = (By.ID, "first-name")
    LAST_NAME_INPUT = (By.ID, "last-name")
    POSTAL_CODE_INPUT = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")

    @allure.step("Ввод имени: {first_name}")
    def enter_first_name(self, first_name):
        self.driver.find_element(*self.FIRST_NAME_INPUT).send_keys(first_name)

    @allure.step("Ввод фамилии: {last_name}")
    def enter_last_name(self, last_name):
        self.driver.find_element(*self.LAST_NAME_INPUT).send_keys(last_name)

    @allure.step("Ввод почтового индекса: {postal_code}")
    def enter_postal_code(self, postal_code):
        self.driver.find_element(*self.POSTAL_CODE_INPUT).send_keys(postal_code)

    @allure.step("Клик по кнопке Continue")
    def click_continue(self):
        self.click_element(self.CONTINUE_BUTTON)
        return CheckoutTwoPage(self.driver)
