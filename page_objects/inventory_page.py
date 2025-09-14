# page_objects/inventory_page.py
from selenium.webdriver.common.by import By

class InventoryPage:
    def __init__(self, driver):
        self.driver = driver
        self.header_title = (By.CLASS_NAME, "title")
        self.add_to_cart_button = (By.ID, "add-to-cart-sauce-labs-backpack")
        self.shopping_cart_link = (By.CLASS_NAME, "shopping_cart_link")

    def is_inventory_page_displayed(self):
        return self.driver.find_element(*self.header_title).is_displayed()

    def add_backpack_to_cart(self):
        self.driver.find_element(*self.add_to_cart_button).click()

    def go_to_shopping_cart(self):
        self.driver.find_element(*self.shopping_cart_link).click()