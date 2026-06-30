import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

def test_success_login(driver):
    """Тест 1: Чистая проверка логина"""
    login_page = LoginPage(driver)
    login_page.open_page()
    login_page.login("standard_user", "secret_sauce")
    assert "inventory.html" in driver.current_url

@pytest.mark.parametrize("product", ["backpack", "bike-light", "bolt-t-shirt"])
def test_add_product_to_cart(logged_in_inventory_page, product):
    """Тест 2: Добавление разных товаров в корзину через параметризацию"""
    inventory_page = logged_in_inventory_page
    
    assert inventory_page.get_title_text() == "Products"
    
    inventory_page.add_product_to_cart_by_name(product)
    
    assert inventory_page.get_cart_badge_text() == "1"


def test_remove_product_from_cart(logged_in_inventory_page):
    """Тест 3: Удаление товара из корзины"""
    inventory_page = logged_in_inventory_page
    
    inventory_page.add_product_to_cart_by_name("backpack")
    assert inventory_page.get_cart_badge_text() == "1"
    
    inventory_page.remove_product_from_cart_by_name("backpack")
    
    assert inventory_page.get_cart_badge_text() == "0"
