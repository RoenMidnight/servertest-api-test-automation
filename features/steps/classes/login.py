import requests
import random, string
from classes.usuario import Usuario

class Login:        
    def do_request(context, request, data):
        if "given" in data:     
            usuario = Usuario().do_request(context, "GET", "given").json()       
            body = { "email": usuario["email"], "password": usuario["password"] }
        
        if "invalid_email" in data:
            body = { "email": "InvalidEmail@qa.com", "password": "InvalidPassWord" }

        if "invalid_password" in data:
            usuario = Usuario().do_request(context, "GET", "given").json()  
            body = { "email": usuario["email"], "password": "InvalidPassWord" }
                
        url = context.base_url + "login/"        

        context.request_data = requests.post(url, headers=context.headers, json=body)

        if "authorization" in context.request_data:
            context.bearer_token = context.request_data.json()["authorization"]

        return context.request_data


    