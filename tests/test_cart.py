import allure

@allure.epic("Корзина товаров")
@allure.feature("Навигация")
@allure.story("Переход в корзину из каталога")
@allure.title("Успешный переход в корзину по клику на иконку тележки")
def test_navigate_to_cart_page(logged_in_inventory_page):
    # 1. Фикстура дает нам готовый объект страницы каталога
    inventory_page = logged_in_inventory_page

    # 2. Кликаем по корзине. Метод click_cart() сам вернет нам объект CartPage
    cart_page = inventory_page.click_cart()

    # 3. Делаем финальную проверку (assert) уже на новой странице
    with allure.step("Проверка, что заголовок страницы изменился на 'Your Cart'"):
        assert cart_page.get_title_text() == "Your Cart"

@allure.epic("Корзина товаров")
@allure.feature("Счетчик товаров")
@allure.story("Добавление нескольких позиций")
@allure.title("Проверка корректного подсчета нескольких товаров в корзине")
def test_add_multiple_products_to_cart(logged_in_inventory_page):
    inventory_page = logged_in_inventory_page

    # 1. Добавляем рюкзак и проверяем промежуточный результат
    inventory_page.add_product_to_cart_by_name("backpack")
    
    with allure.step("Проверка, что после добавления рюкзака на счетчике отображается '1'"):
        assert inventory_page.get_cart_badge_text() == "1"

    # 2. Добавляем футболку
    inventory_page.add_product_to_cart_by_name("bolt-t-shirt")

    # 3. Финальная проверка, что счетчик стал равен 2
    with allure.step("Проверка, что после добавления второго товара на счетчике отображается '2'"):
        assert inventory_page.get_cart_badge_text() == "2"
