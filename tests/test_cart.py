import allure

@allure.epic("Корзина товаров")
@allure.feature("Навигация")
@allure.story("Переход в корзину из каталога")
@allure.title("Успешный переход в корзину по клику на иконку тележки")
def test_navigate_to_cart_page(logged_in_inventory_page):
    
    inventory_page = logged_in_inventory_page

    cart_page = inventory_page.click_cart()

    with allure.step("Проверка, что заголовок страницы изменился на 'Your Cart'"):
        assert cart_page.get_title_text() == "Your Cart"

@allure.epic("Корзина товаров")
@allure.feature("Счетчик товаров")
@allure.story("Добавление нескольких позиций")
@allure.title("Проверка корректного подсчета нескольких товаров в корзине")
def test_add_multiple_products_to_cart(logged_in_inventory_page):
    inventory_page = logged_in_inventory_page

    
    inventory_page.add_product_to_cart_by_name("backpack")
    
    with allure.step("Проверка, что после добавления рюкзака на счетчике отображается '1'"):
        assert inventory_page.get_cart_badge_text() == "1"

    inventory_page.add_product_to_cart_by_name("bolt-t-shirt")

    with allure.step("Проверка, что после добавления второго товара на счетчике отображается '2'"):
        assert inventory_page.get_cart_badge_text() == "2"
