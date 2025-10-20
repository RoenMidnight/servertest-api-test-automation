Feature: Happy Path to CRUD flow to Users

    Scenario: GET - List of All Users
        When I do a "GET" request to "usuario" endpoint with "empty" data
        Then the status code should be "200"
        And a list of "usuario" should be returned
    
    Scenario: GET - A User Data
        Given I create a new "usuario"
        When I do a "GET" request to "usuario" endpoint with "given" data
        Then the status code should be "200"
        And the response should be return a "usuario" object

    Scenario: POST - Create a New User
        When I do a "POST" request to "usuario" endpoint with "base" data
        Then the status code should be "201"
        And the "message" with "Cadastro realizado com sucesso" is on response body
        And the "_id" property in the response should not be empty

    Scenario: PUT - Update a User Data
        Given I create a new "usuario"
        When I do a "PUT" request to "usuario" endpoint with "update" data 
        Then the status code should be "200"
        And the "message" with "Registro alterado com sucesso" is on response body
        And validate if the "usuario" data was "updated" on the server

    Scenario: PUT - Create a New User when the User ID is Invalid
        When I do a "PUT" request to "usuario" endpoint with "base" data
        Then the status code should be "201"
        And the "message" with "Cadastro realizado com sucesso" is on response body
        And the "_id" property in the response should not be empty

    Scenario: DEL - Delete a existing User
        Given I create a new "usuario"
        When I do a "DEL" request to "usuario" endpoint with "given" data
        And the "message" with "Registro excluído com sucesso" is on response body
        And validate if the "usuario" data was "deleted" on the server
        And the "message" with "Usuário não encontrado" is on response body