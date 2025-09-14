
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions


def pytest_addoption(parser):
    """This function adds a command-line option to specify the browser."""
    parser.addoption(
        "--browser", action="store", default="chrome", help="Specify browser: chrome or firefox"
    )


@pytest.fixture
def driver(request):
    """This fixture creates a WebDriver instance based on the --browser option."""
    browser_name = request.config.getoption("browser").lower()

    if browser_name == "chrome":

        chrome_options = ChromeOptions()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")  # A must-have for running as root in Docker/CI
        chrome_options.add_argument("--disable-dev-shm-usage")  # Overcomes limited resource problems
        chrome_options.add_argument("--window-size=1920,1080")  # Ensures a consistent window size
        driver = webdriver.Chrome(options=chrome_options)
    elif browser_name == "firefox":

        firefox_options = FirefoxOptions()
        firefox_options.add_argument("--headless")
        driver = webdriver.Firefox(options=firefox_options)
    else:
        raise pytest.UsageError(f"--browser={browser_name} is not a valid option")

    driver.implicitly_wait(10)
    driver.get("https://www.saucedemo.com/")
    yield driver
    driver.quit()
