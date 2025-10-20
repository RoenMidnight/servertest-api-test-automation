from behave import *
from classes.usuario import Usuario
from classes.login import Login
from utils import api_calls

@given('I create a new "{object}"')
def step_impl(context, object):
    if object == "usuario":
        context.usuario = Usuario()
        api_calls.create_new_obj(context, "usuarios", context.usuario.return_usuario())


@when('I do a "{request}" request to "{endpoint}" endpoint with "{data}" data')
def step_impl(context, request, endpoint, data):
    if endpoint == "usuario":
        if "usuario" not in context:
            context.usuario = Usuario()
            
        context.request_data = context.usuario.do_request(context, request, data)
    if endpoint == "login":
        if "usuario" not in context:
            context.usuario = Usuario()
        Login.do_request(context, request, data)

@then('the status code should be "{code}"')
def step_impl(context, code):
    assert context.request_data.status_code == int(code)

@step('a list of "{endpoint}" should be returned')
def step_impl(context, endpoint):
    if endpoint == "usuario":      
        assert context.usuario.validate_if_is_usuario(context.request_data.json()["usuarios"][0])

@step('the "{property}" property in the response should not be empty')
def step_impl(context, property):
    assert property in context.request_data.json()
    assert context.request_data.json()[property] is not None

@step('the "{field}" with "{message}" is on response body')
def step_impl(context, field, message):
    assert message == context.request_data.json()[field]

@step('validate if the "{endpoint}" data was "{action}" on the server')
def step_impl(context, endpoint, action):
    if endpoint == "usuario":
        server_data = context.usuario.do_request(context, "GET", "given")

        if action == "updated":
            body_data = context.usuario.return_usuario()
            server_data = server_data.json()
            assert body_data["nome"] == server_data["nome"]
            assert body_data["email"] == server_data["email"]
            assert body_data["password"] == server_data["password"]
            assert body_data["administrador"] == server_data["administrador"]
        
        if action == "deleted":
            context.request_data = server_data

@step('the response should be return a "{object}" object')
def step_impl(context, object):
    if object == "usuario":
        assert context.usuario.validate_if_is_usuario(context.request_data.json())


@when('I do "{times}" "{request}" requests to "{endpoint}" endpoint with "{data}" data')
def step_impl(context, times, request, endpoint, data):
    if endpoint == "usuario":
        if "usuario" not in context:
            context.usuario = Usuario()
            for i in range(1, int(times)):
                context.usuario.do_request(context, request, data)
