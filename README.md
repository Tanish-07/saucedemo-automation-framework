# End-to-End Test Automation Framework for Sauce Labs Demo

![CI/CD Pipeline](https://github.com/Tanish-07/saucedemo-automation-framework/actions/workflows/ci.yml/badge.svg)

## Overview

This project is a robust test automation framework built from the ground up to test the Sauce Labs Demo e-commerce website, "[Swag Labs](https://www.saucedemo.com/)". The framework is designed to be scalable, maintainable, and demonstrates best practices in QA automation by covering critical user flows and integrating modern development tools.

The entire project was managed using **Agile/Scrum methodologies in Jira**, where test scenarios were documented as user stories, planned in sprints, and tracked on a Scrum board.

---

## 🚀 Key Features

### Automated Scenarios
* **User Authentication:** Validates successful login with standard user credentials and verifies correct error handling for failed login attempts.
* **Shopping Cart Management:** Covers the end-to-end flow of adding a specific item ("Sauce Labs Backpack") to the cart and verifying its presence.
* **Data-Driven Testing:** Credentials and other test data are managed externally in a `config.ini` file, not hardcoded in the test scripts.

### Framework Features
* **Page Object Model (POM):** The framework is built on the Page Object Model design pattern, ensuring a clean separation between test logic and UI element locators for high maintainability.
* **Cross-Browser Testing:** Tests are configured to run on multiple browsers (Chrome and Firefox) using a single command-line argument.
* **Interactive Test Reports:** Integrated with **Allure Report** to generate detailed, easy-to-read HTML reports with test steps, statuses, and execution times.
* **Continuous Integration/Continuous Deployment (CI/CD):** The project includes a **GitHub Actions** workflow that automatically triggers the entire test suite on every push and pull request to the `main` branch.

---

## 🛠️ Tech Stack & Tools

* **Programming Language:** Python 3.11+
* **Test Automation Library:** Selenium
* **Test Runner:** Pytest
* **Reporting:** Allure Report
* **CI/CD:** GitHub Actions
* **Project Management:** Jira (Agile/Scrum)

---

## 📁 Project Structure

The project follows a standardized and organized structure to promote scalability and ease of navigation.

```
saucedemo_automation/
├── .github/
│   └── workflows/
│       └── ci.yml             # GitHub Actions CI/CD workflow
├── page_objects/              # Contains all Page Object classes
│   ├── login_page.py
│   ├── inventory_page.py
│   └── cart_page.py
├── tests/                     # Contains all test scripts
│   ├── test_login.py
│   └── test_shopping_cart.py
├── utils/                     # Helper utilities
│   └── config_reader.py
├── conftest.py                # Pytest fixtures and configurations
├── config.ini                 # Configuration file for test data
├── requirements.txt           # Project dependencies
└── README.md                  # You are here!
```

---

## 🏁 Getting Started

Follow these instructions to set up the project and run the tests on your local machine.

### Prerequisites

* Python 3.11+ installed
* Git installed
* Google Chrome and/or Mozilla Firefox installed

### Installation & Setup

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/Tanish-07/saucedemo-automation-framework.git](https://github.com/Tanish-07/saucedemo-automation-framework.git)
    ```

2.  **Navigate to the project directory:**
    ```bash
    cd saucedemo-automation-framework
    ```

3.  **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

---

## ▶️ How to Run the Tests

Tests can be executed directly from the terminal.

### Basic Execution
To run the entire test suite on the default browser (Chrome):
```bash
pytest
```

### Cross-Browser Execution
To run the tests on a specific browser, use the `--browser` flag:

* **Run on Chrome:**
    ```bash
    pytest --browser chrome
    ```

* **Run on Firefox:**
    ```bash
    pytest --browser firefox
    ```

---

## 📊 Test Reporting with Allure

This project uses Allure to generate detailed and interactive test reports.


### Generating the Report

1.  **Run Pytest and generate Allure results:**
    ```bash
    pytest --alluredir=./reports
    ```
    This command runs the tests and saves the result data in the `reports` directory.

2.  **Serve the Allure report:**
    ```bash
    allure serve ./reports
    ```
    This command will generate and open the HTML report in your default web browser.
