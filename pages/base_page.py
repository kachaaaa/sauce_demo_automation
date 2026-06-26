class BasePage:
    def __init__(self, driver):
        """Базовый конструктор, который передает драйвер всем страницам"""
        self.driver = driver

    def open_url(self, url):
        """Общий метод для открытия любой ссылки"""
        self.driver.get(url)

import allure  # Импортируем Allure для разметки шагов

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    # Описываем шаг для отчёта. Текст в кавычках будет красиво отображаться в Allure
    @allure.step("Переход по адресу: {url}")
    def open_url(self, url):
        """Общий метод для открытия любой ссылки"""
        self.driver.get(url)
