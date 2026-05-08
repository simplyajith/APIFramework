# APIFramework

## Overview
This is a pytest-based API testing framework. It utilizes Allure for detailed reporting.

## Setup
1. Ensure you have Python installed.
2. Activate your virtual environment (`.venv`).
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Make sure you have the Allure command-line tool installed on your system to generate and view the reports.

## Running Tests and Generating Reports

1. **Run tests and collect results:**
   Execute your test suite using pytest and specify the directory to save the raw allure results:
   ```bash
   pytest --alluredir=test-result
   ```

2. **Generate the Allure HTML report:**
   After the test execution is complete, generate the HTML report from the results directory:
   ```bash
   allure generate test-result -o allure-report --clean
   ```

3. **View the Allure report:**
   You can view the generated report by opening it directly from the `allure-report` folder or using the allure serve command:
   ```bash
   allure serve test-result
   ```
