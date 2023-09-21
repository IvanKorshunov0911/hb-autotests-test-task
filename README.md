# HomeBuddy: HVAC page autotests

Contains Selenium+Pytest tests for /hvac page of HomeBuddy

## Table of Contents

- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
  - [Installation](#installation)
  - [Configuration](#configuration)
- [Usage](#usage)
- [Running Tests](#running-tests)
- [Multithreading](#multithreading)
- [Contributing](#contributing)
- [License](#license)

## Prerequisites

List any prerequisites here, including software, dependencies, and any special configuration needed.

- Python 3.x
- Selenium WebDriver

## Getting Started

Explain how to get started with your project. Include step-by-step instructions to set up the environment and any initial configuration needed.

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/IvanKorshunov0911/hb-autotests-test-task.git
   ```

2. Install requirements:
    ```bash
   cd your-repo
    pip install -r requirements.txt
   ```
   
## Running Tests

To run the tests, make sure you have installed the project dependencies (as explained in the [Installation](#installation) section) and configured any necessary settings.

You can use pytest to run your tests. By default, pytest will discover and run all test files matching the pattern `test_*.py`. To execute the tests, open a terminal in the project directory and run the following command:

```bash
pytest
```

This will execute all the tests in your project.

### Running Specific Tests
If you want to run specific tests or a specific test file, you can specify the test file or directory as an argument to pytest. For example, to run a specific test file:
```bash
pytest path/to/your/test_file.py
```
For example:
```bash
pytest pytest test_hvac_page.py
```
### Test Reports and Output
By default, pytest provides detailed information about test results, including any failures or errors. You can also generate html test reports by using the following command:
```bash
pytest --html-report=./report/report.html
```

### Multithreading
To run tests in parallel using pytest, you can use the `pytest-xdist` plugin. It is installed from requirements.txt in the [Installation](#installation) section)

Run pytest with the desired number of threads using the -n option. For example, to run tests in four parallel threads:
```bash
pytest -n 4
```
### URL
URL may be changed in test_hvac_page.py

### GUI / Headless mode
By passing flag --gui y tests may be run not in headless mode:
```bash
pytest --gui y
```
### Test command example:
```bash
pytest -n 8 --html-report=./report/report.html --gui y test_hvac_page.py
```