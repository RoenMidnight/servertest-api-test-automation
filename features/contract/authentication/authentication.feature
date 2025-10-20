Feature: Happy Get JWT Token Flow

    Scenario: GET - JWT Token
        Given I create a new "usuario"
        When I do a "GET" request to "login" endpoint with "given" data
        Then the status code should be "200"
        And the "message" with "Login realizado com sucesso" is on response body