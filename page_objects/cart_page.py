
from selenium.webdriver.common.by import By

class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.item_name = (By.CLASS_NAME, "inventory_item_name")

    def get_item_name_in_cart(self):
        return self.driver.find_element(*self.item_name).text
