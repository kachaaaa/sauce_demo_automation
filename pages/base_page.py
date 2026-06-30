import allure  

class BasePage:
    def __init__(self, driver):
        self.driver = driver
    
    @allure.step("Открытие URL: {url}")
    def open_url(self, url):
        self.driver.get(url)

    def click_element(self, locator):
        self.driver.find_element(*locator).click()
