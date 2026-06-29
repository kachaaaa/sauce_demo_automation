# SauceDemo UI Automation Framework

A scalable and highly maintainable automated UI testing framework built with Python, pytest, and Selenium WebDriver for the [SauceDemo](https://www.saucedemo.com/) e-commerce platform.

## 🚀 Key Features & Architectural Highlights

- **Page Object Model (POM):** Strict separation of test logic from UI elements and actions, ensuring clean, scalable, and modular code.
- **Robust Base Components:** Implemented a unified BasePage that handles web driver interaction logic, eliminating code redundancy and adhering to DRY principles.
- **Smart Lifecycles with Pytest Fixtures:** Centralized browser initialization, cross-test configurations, and pre-authorized session hooks managed inside `tests/conftest.py`.
- **Data-Driven Testing (Parametrization):** Maximized test coverage using `@pytest.mark.parametrize` to execute identical scripts across multiple data layers.
- **Advanced Allure Reports:** Integrated Allure Framework featuring detailed execution graphs, custom annotations (`@allure.step`, `@allure.epic`, `@allure.feature`), and dynamic argument logging for granular debugging.

## 🛠️ Tech Stack

- **Language:** Python 3.12+
- **Test Runner:** pytest
- **Automation Tool:** Selenium WebDriver
- **Reporting:** Allure Framework

## 📁 Project Structure

```text
sauce_demo_automation/
│
├── pages/
│   ├── base_page.py             # Parent page object with shared locator actions
│   ├── login_page.py            # Login page elements and methods
│   ├── inventory_page.py        # Product catalog page elements and actions
│   └── cart_page.py             # Cart page elements, badges, and validation actions
│
├── tests/
│   ├── conftest.py              # Global pytest fixtures and driver configuration
│   ├── test_login.py            # Authentication test scenarios
│   └── test_cart.py             # Shopping cart item and badge counter test scenarios
│
├── .gitignore                   # Excludes venv, pycache, and local allure logs
├── requirements.txt             # Project dependencies and libraries
├── test_sandbox.py              # Sandbox file for quick testing/experiments
└── README.md                    # Project documentation

🎯 Test Coverage & Scenarios

🔐 Authentication (tests/test_login.py)
Positive end-to-end authentication scenarios using valid standard user credentials.
Negative test scenarios verifying form validation, error message indicators, and locked-out user restrictions.
🛒 Shopping Cart (tests/test_cart.py)
Navigation Verification: Validating seamless redirection from the product catalog to the Cart page using the header shopping cart icon.
Dynamic Item Counter: Testing dynamic badge item calculations via specialized locator structures to handle multi-product additions correctly.

💻 Installation & Local Setup

1.Clone the repository:
git clone [https://github.com/kachaaaa/sauce_demo_automation.git](https://github.com/kachaaaa/sauce_demo_automation.git)
cd sauce_demo_automation

2.Set up a Virtual Environment:
python3 -m venv venv
source venv/bin/activate  # On macOS/Linux
# venv\Scripts\activate   # On Windows

3.Install Dependencies:
pip install -r requirements.txt

📊 Running Tests & Reporting
Run all tests sequentially:
pytest

Run tests and view interactive Allure Reports:
pytest --alluredir=allure-results
allure serve allure-results

