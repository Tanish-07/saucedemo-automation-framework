# tests/test_login.py
from page_objects.login_page import LoginPage
from page_objects.inventory_page import InventoryPage


# The file now starts directly with the tests.
# Pytest will automatically find the 'driver' fixture in conftest.py

# Test Case 1: Successful Login
def test_successful_login(driver):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)

    # Perform login
    login_page.enter_username("standard_user")
    login_page.enter_password("secret_sauce")
    login_page.click_login()

    # Assert that we are on the inventory page
    assert inventory_page.is_inventory_page_displayed(), "Login failed and inventory page was not displayed."


# Test Case 2: Failed Login
def test_failed_login(driver):
    login_page = LoginPage(driver)

    # Perform login with wrong credentials
    login_page.enter_username("standard_user")
    login_page.enter_password("wrong_password")
    login_page.click_login()

    # Assert that the correct error message is shown
    expected_error = "Epic sadface: Username and password do not match any user in this service"
    actual_error = login_page.get_error_message()
    assert actual_error == expected_error, f"Error message was incorrect. Expected '{expected_error}', but got '{actual_error}'."