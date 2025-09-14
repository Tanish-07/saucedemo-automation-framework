# tests/test_login.py

# Notice we only import what's needed for the test logic
from page_objects.login_page import LoginPage
from page_objects.inventory_page import InventoryPage
from utils.config_reader import read_config


# The driver fixture is now automatically used from conftest.py

def test_successful_login(driver):
    """
    Tests a successful login using standard user credentials from the config file.
    """
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)

    # Get username and password from the config file
    username = read_config("Credentials", "standard_user")
    password = read_config("Credentials", "password")

    # Perform login
    login_page.enter_username(username)
    login_page.enter_password(password)
    login_page.click_login()

    # Assert that we are on the inventory page
    assert inventory_page.is_inventory_page_displayed(), "Login failed: Inventory page not displayed."


def test_failed_login_with_wrong_password(driver):
    """
    Tests a failed login attempt using a wrong password.
    """
    login_page = LoginPage(driver)

    # Get username from config, but use a deliberate wrong password
    username = read_config("Credentials", "standard_user")

    # Perform login with wrong credentials
    login_page.enter_username(username)
    login_page.enter_password("wrong_password")
    login_page.click_login()

    # Assert that the correct error message is shown
    expected_error = "Epic sadface: Username and password do not match any user in this service"
    actual_error = login_page.get_error_message()
    assert actual_error == expected_error, f"Error message was incorrect. Expected '{expected_error}', but got '{actual_error}'."