import pytest
from selenium import webdriver
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

@pytest.fixture
def driver():
    """Базовая фикстура для запуска браузера Chrome"""
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()

@pytest.fixture
def logged_in_inventory_page(driver):
    """Фикстура автоматической авторизации. Возвращает объект InventoryPage"""
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    
    login_page.open_page()
    login_page.login("standard_user", "secret_sauce")
    
    return inventory_page
