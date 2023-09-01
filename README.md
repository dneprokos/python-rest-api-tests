# python-rest-api-tests project

This Project design to pratice in creation of REST API tests using Python programming language

![Config file](/images/Rest_vs_Python.png)

# Setup Instructions

## Python Setup

- Install Python of version "3.11" or higher from [Python.org](https://www.python.org/downloads/). Don't forget to include it to PATH variables
- Install pipenv, run `pip install pipenv` from the command line.

## Install dependencies

- In the root of the repository, run "pipenv install" from the command line.

##  Activate a virtual environment

- Run "pipenv shell" from command line to activate virtual environment

# Application used for Testing

- Please pull "https://github.com/dneprokos/node-rest-services" git repository and follow README.md installation and run intructions

## Run tests

- Run command `pipenv run python -m pytest` from the command line to run all the tests

- Run command `pipenv run python -m pytest -s` from command line to run all the tests and see all printed outputs

- Run command `pipenv run python -m pytest -n 5` from command line in order to run all tests in parallel. Number "5" can be changed to expected number of threads

- Run command `pipenv run python -m pytest --alluredir=allure_reports` from command line in order to generate allure-reports. Directory name can be changed

## Show allure reports

- Allure command line should be installed: https://docs.qameta.io/allure/#_installing_a_commandline
- Tests should be run with allure flag
- Run command `allure serve allure_reports`. - Last part is a path to directory with generated reports

![Report example](/images/report.png)