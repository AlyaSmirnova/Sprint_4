# 📚 BooksCollector: Unit Testing Framework

![CI/CD Status](https://github.com)
[![Python Version](https://img.shields.io)](https://www.python.org)
[![Testing Framework](https://img.shields.io)](https://docs.pytest.org)
[![Reporting](https://img.shields.io)](https://github.com)

## 🎯 Project Overview
This repository showcases an approach to unit testing for the **BooksCollector** application. The project implements a scalable testing architecture with deep reporting and automated validation.
The test suite ensures 100% reliability of core features: book inventory, genre categorization (including age-rating logic), and user favorites management.

## 🧑‍💻 Tech Stack & Tools
- **Language:** Python 3.10+
- **Testing:** `pytest` (utilizing fixtures, parametrization, and clean code principles)
- **Reporting:** `Allure Framework` (rich, human-readable HTML reports)
- **CI/CD:** `GitHub Actions` (automated test execution on every push)

## 📁 Project Architecture
The project is organized to ensure clean code separation and transparency:
```text
Sprint_4/
    ├── .github/workflows/        # CI/CD pipeline configuration (GitHub Actions)
    ├── allure-results/           # Raw test execution data (generated after run)
    ├── main.py                   # Core application logic (BooksCollector class)
    ├── tests.py                  # Unit test suite with Allure annotations & fixtures
    ├── requirements.txt          # List of project dependencies
    └── README.md                 # Comprehensive project documentation
```

## 📊 Allure Reporting Features
I have integrated the **Allure Framework** to provide high-level visibility into test execution and simplify debugging:

- **Dynamic Test Titles:** Uses `@allure.title` to generate descriptive, human-readable test names that automatically update based on input parameters.
- **Granular Execution Steps:** Implements `@allure.step` annotations to track the logic flow within each test, making it easy to pinpoint exactly where a failure occurred.
- **Logical Test Suites:** Categorizes tests into functional suites using `@allure.suite` for better navigation and structured analysis of the test results.
- **Environment Details:** Provides a clear overview of the test environment and execution parameters.

## 🚀 Execution Guide

### 1. Environment Setup
Clone the repository and set up a local virtual environment to ensure dependency isolation:

1. **Clone repository**
> ```bash 
> git clone https://github.com/AlyaSmirnova/Sprint_4
> cd Sprint_4
📦 Repository: [Sprint_4](https://github.com/AlyaSmirnova/Sprint_4)

2. **Create a virtual environment**
> ```bash 
> python -m venv venv

3. **Activate the virtual environment**
> ```bash 
> source venv/bin/activate

4. **Install required dependencies**
> `$ pip install -r requirements.txt`

### 2. Running Tests
Execute the full test suite and collect raw data for the Allure report:
> ```bash 
> pytest -v --alluredir=allure-results

### 3. Generatig Allure Report
Transform the raw data into a visual, interactive HTML report:
> ```bash 
> allure serve allure-results