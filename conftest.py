# conftest.py
import pytest
from selenium import webdriver

def pytest_addoption(parser):
    """This function adds a command-line option to specify the browser."""
    parser.addoption(
        "--browser", action="store", default="chrome", help="Specify browser: chrome or firefox"
    )

@pytest.fixture
def driver(request):
    """This fixture creates a WebDriver instance based on the --browser option."""
    browser_name = request.config.getoption("browser")
    if browser_name.lower() == "chrome":
        driver = webdriver.Chrome()
    elif browser_name.lower() == "firefox":
        # Make sure you have geckodriver installed for Firefox
        driver = webdriver.Firefox()
    else:
        raise pytest.UsageError(f"--browser={browser_name} is not a valid option")

    driver.implicitly_wait(10)
    driver.get("https://www.saucedemo.com/")
    yield driver
    driver.quit()