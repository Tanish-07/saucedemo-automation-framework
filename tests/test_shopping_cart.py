# tests/test_shopping_cart.py
from page_objects.login_page import LoginPage
from page_objects.inventory_page import InventoryPage
from page_objects.cart_page import CartPage


def test_add_item_to_cart(driver):
    # 1. Arrange - Set up the pages
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)

    # Expected item name
    expected_item_name = "Sauce Labs Backpack"

    # 2. Act - Perform the actions
    login_page.enter_username("standard_user")
    login_page.enter_password("secret_sauce")
    login_page.click_login()

    inventory_page.add_backpack_to_cart()
    inventory_page.go_to_shopping_cart()

    actual_item_name = cart_page.get_item_name_in_cart()

    # 3. Assert - Verify the outcome
    assert actual_item_name == expected_item_name, \
        f"Expected item '{expected_item_name}' but found '{actual_item_name}' in cart."