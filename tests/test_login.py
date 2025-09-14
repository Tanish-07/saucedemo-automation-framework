
from page_objects.login_page import LoginPage
from page_objects.inventory_page import InventoryPage
from utils.config_reader import read_config




def test_successful_login(driver):
    """
    Tests a successful login using standard user credentials from the config file.
    """
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)


    username = read_config("Credentials", "standard_user")
    password = read_config("Credentials", "password")


    login_page.enter_username(username)
    login_page.enter_password(password)
    login_page.click_login()


    assert inventory_page.is_inventory_page_displayed(), "Login failed: Inventory page not displayed."


def test_failed_login_with_wrong_password(driver):
    """
    Tests a failed login attempt using a wrong password.
    """
    login_page = LoginPage(driver)

    username = read_config("Credentials", "standard_user")

    login_page.enter_username(username)
    login_page.enter_password("wrong_password")
    login_page.click_login()

    # Assert that the correct error message is shown
    expected_error = "Epic sadface: Username and password do not match any user in this service"
    actual_error = login_page.get_error_message()
    assert actual_error == expected_error, f"Error message was incorrect. Expected '{expected_error}', but got '{actual_error}'."
