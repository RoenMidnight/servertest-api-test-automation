[![Badge ServeRest](https://img.shields.io/badge/API-ServeRest-green)](https://github.com/ServeRest/ServeRest/)
[![Run API Tests](https://github.com/RoenMidnight/servertest-api-test-automation/actions/workflows/behave_tests.yml/badge.svg)](https://github.com/RoenMidnight/servertest-api-test-automation/actions/workflows/behave_tests.yml)


# Automated Tests to API Serverest

This project do automated tests to [https://serverest.dev](https://serverest.dev) API with the following tools: 

- Python
- Behave (BDD)
- Faker (Generate Fake Data)
- GitHub Actions (CI/CD)
- Allure Reports

## How to run at your local environment
```bash
git clone https://github.com/RoenMidnight/servertest-api-test-automation.git
cd project-api-automation-serverest
pip install -r requirements.txt
behave --exclude="performance.feature" ./features 
```

## How to generante and access the Reports
```bash
behave -f allure_behave.formatter:AllureFormatter -o allure_results --exclude="performance.feature" ./features
```

## Test Structure
The test cases are divided in Contract, End To End and Performance and this tests are divided between Happy and Negative Paths.

-`features/contract`: contract test cases feature files;
-`features/endToEnd`: end to end test cases feature files;
-`features/performance`: performance test cases feature files;
-`features/enviroment.py`: set environment variables and run pre-condition to tests 
-`features/steps/classes`: project classes with methods
-`features/steps/general.steps.py`: test steps implementation

## Pipeline GitHub Actions
Every `push` or `pull_request` done on `main` authomatic run:

1. Instalation of Depencies
2. Test Execution
3. Report Generation
4. Artifact Upload


## Autor
- Bruno Cesar Alves de Freitas Ferreira Mendes
- Desafio de Automação de Testes para Serverest API