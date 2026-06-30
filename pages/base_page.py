import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        
        self.wait = WebDriverWait(driver, timeout)
    
    @allure.step("Открытие URL: {url}")
    def open_url(self, url):
        self.driver.get(url)

    def click_element(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()
        
    def find_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))
