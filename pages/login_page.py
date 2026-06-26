import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")

    @allure.step("Открытие главной страницы авторизации")
    def open_page(self):
        self.open_url("https://www.saucedemo.com/")

    # Здесь мы тоже динамически выводим логин в отчёт, чтобы видеть, под кем заходили
    @allure.step("Авторизация пользователем: {username}")
    def login(self, username, password):
        self.driver.find_element(*self.USERNAME_INPUT).send_keys(username)
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)
        self.driver.find_element(*self.LOGIN_BUTTON).click()
