import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_saucedemo_login():
    # 1. Запускаем браузер Chrome
    driver = webdriver.Chrome()
    
    # 2. Открываем сайт
    driver.get("https://www.saucedemo.com/")
    
    # 3. Находим поле Username по нашему data-test селектору и вводим валидный логин
    username_field = driver.find_element(By.CSS_SELECTOR, '[data-test="username"]')
    username_field.send_keys("standard_user")
    
    # 4. Находим поле Password и вводим пароль
    password_field = driver.find_element(By.CSS_SELECTOR, '[data-test="password"]')
    password_field.send_keys("secret_sauce")
    
    # 5. Находим кнопку Login и кликаем по ней
    login_button = driver.find_element(By.CSS_SELECTOR, '[data-test="login-button"]')
    login_button.click()
    
    # 6. Ожидаемый результат: проверяем, что мы перешли на страницу инвентаря (магазина)
    current_url = driver.current_url
    assert "inventory.html" in current_url, f"Ошибка! Ожидали inventory.html, но получили {current_url}"
    
    # 7. Закрываем браузер
    driver.quit()


def test_saucedemo_invalid_login():
    # 1. Запускаем браузер
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    
    # 2. Вводим верный логин, но НЕВЕРНЫЙ пароль
    driver.find_element(By.CSS_SELECTOR, '[data-test="username"]').send_keys("standard_user")
    driver.find_element(By.CSS_SELECTOR, '[data-test="password"]').send_keys("wrong_password")
    driver.find_element(By.CSS_SELECTOR, '[data-test="login-button"]').click()
    
    # 3. Находим элемент ошибки с помощью XPATH
    error_element = driver.find_element(By.XPATH, '//h3[@data-test="error"]')
    
    # 4. Вытаскиваем из элемента живой текст
    error_text = error_element.text
    
    # 5. Проверяем (assert), что текст ошибки именно такой, какой мы ожидали
    expected_error = "Epic sadface: Username and password do not match any user in this service"
    assert error_text == expected_error, f"Ожидали ошибку '{expected_error}', но получили '{error_text}'"
    
    # 6. Закрываем браузер
    driver.quit()
