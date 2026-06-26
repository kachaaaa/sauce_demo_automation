import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_saucedemo_login():

    driver = webdriver.Chrome()
    
    driver.get("https://www.saucedemo.com/")
    
    username_field = driver.find_element(By.CSS_SELECTOR, '[data-test="username"]')
    username_field.send_keys("standard_user")
    
    password_field = driver.find_element(By.CSS_SELECTOR, '[data-test="password"]')
    password_field.send_keys("secret_sauce")
    
    login_button = driver.find_element(By.CSS_SELECTOR, '[data-test="login-button"]')
    login_button.click()
    
    current_url = driver.current_url
    assert "inventory.html" in current_url, f"Ошибка! Ожидали inventory.html, но получили {current_url}"
    
    driver.quit()


def test_saucedemo_invalid_login():
    
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    
    driver.find_element(By.CSS_SELECTOR, '[data-test="username"]').send_keys("standard_user")
    driver.find_element(By.CSS_SELECTOR, '[data-test="password"]').send_keys("wrong_password")
    driver.find_element(By.CSS_SELECTOR, '[data-test="login-button"]').click()
    
    Находим элемент ошибки с помощью XPATH
    error_element = driver.find_element(By.XPATH, '//h3[@data-test="error"]')
    
    Вытаскиваем из элемента живой текст
    error_text = error_element.text
    
    Проверяем (assert), что текст ошибки именно такой, какой мы ожидали
    expected_error = "Epic sadface: Username and password do not match any user in this service"
    assert error_text == expected_error, f"Ожидали ошибку '{expected_error}', но получили '{error_text}'"
    
    driver.quit()
