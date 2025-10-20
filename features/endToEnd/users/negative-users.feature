Feature: Negative Path to CRUD flow to Users

    Scenario: GET - A non existent User should return error
        When I do a "GET" request to "usuario" endpoint with "invalid_empty_id" data
        Then the status code should be "400"
        And the "message" with "Usuário não encontrado" is on response body

    Scenario: POST - Try to create a user with the same e-mail
        Given I create a new "usuario"
        When I do a "POST" request to "usuario" endpoint with "given" data
        Then the status code should be "400"
        And the "message" with "Este email já está sendo usado" is on response body

    Scenario Outline: POST - Try to create a user with invalid data
        When I do a "POST" request to "usuario" endpoint with "<invalid>" data 
        Then the status code should be "400"
        And the "<field>" with "<response_message>" is on response body
        Examples:
            | invalid                    | response_message                         | field         |
            | invalid_base_nome          | nome não pode ficar em branco            | nome          |
            | invalid_base_email         | email não pode ficar em branco           | email         |
            | invalid_base_password      | password não pode ficar em branco        | password      |
            | invalid_base_administrador | administrador deve ser 'true' ou 'false' | administrador |

    Scenario Outline: PUT - Update User with invalid data
        Given I create a new "usuario"
        When I do a "PUT" request to "usuario" endpoint with "<invalid>" data 
        Then the status code should be "400"
        And the "<field>" with "<response_message>" is on response body
        Examples:
            | invalid                     | response_message                         | field         |
            | invalid_given_nome          | nome não pode ficar em branco            | nome          | 
            | invalid_given_email         | email não pode ficar em branco           | email         |
            | invalid_given_password      | password não pode ficar em branco        | password      | 
            | invalid_given_administrador | administrador deve ser 'true' ou 'false' | administrador |

    Scenario: DEL - Delete a Non Existing User
        When I do a "DEL" request to "usuario" endpoint with "invalid_empty_id" data
        And the "message" with "Nenhum registro excluído" is on response body