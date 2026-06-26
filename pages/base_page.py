class BasePage:
    def __init__(self, driver):
        
        self.driver = driver

    def open_url(self, url):
        
        self.driver.get(url)

import allure  

class BasePage:
    def __init__(self, driver):
        self.driver = driver
    
    @allure.step
    def open_url(self, url):
        
        self.driver.get(url)
