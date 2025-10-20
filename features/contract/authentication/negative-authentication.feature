Feature: Negative Get JWT Token Flow

    Scenario: GET - Try to get Login with Invalid Data
        When I do a "GET" request to "login" endpoint with "invalid_email" data
        Then the status code should be "401"
        And the "message" with "Email e/ou senha inválidos" is on response body

    Scenario: GET - Try to get Login with Invalid Password
        Given I create a new "usuario"
        When I do a "GET" request to "login" endpoint with "invalid_password" data
        Then the status code should be "401"
        And the "message" with "Email e/ou senha inválidos" is on response body