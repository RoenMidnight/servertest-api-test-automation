import requests
import random, string
from faker import Faker

class Usuario:    
    def generate_random_user(self):
        fake = Faker()
        nome = fake.name()
        email = nome.replace(" ", "_") + "@qa.com.br"
        for _ in range(5):
            password = fake.password(length=16)
        administrador = random.choice(["true", "false"])

        return {"nome": nome, "email": email, "password": password, "administrador": administrador}
    
    def __init__(self, nome=None, email=None, password=None, administrador=None):
        random_user = self.generate_random_user()

        self.nome = nome if nome is not None else random_user["nome"]
        self.email = email if email is not None else random_user["email"]
        self.password = password if password is not None else random_user["password"]
        self.administrador = administrador if administrador is not None else random_user["administrador"]    
    
    def return_usuario(self):
        return {"nome": self.nome, "email": self.email, "password": self.password, "administrador": self.administrador}
    
    def validate_if_is_usuario(self, usuario):
        if "nome" not in usuario:
            return False
        if "email" not in usuario:
            return False
        if "password" not in usuario:
            return False
        if "administrador" not in usuario:
            return False
        if "_id" not in usuario:
            return False
        return True
    
    def do_request(self, context, request, data):
        if "empty" in data:
            data = data.replace("empty_", "")
            id = ""
            body = ""
        elif "given" in data:
            data = data.replace("given_", "")
            id = context.given_data.json()["_id"]
            if request == "POST":
                id = ""
            if request in ["POST", "PUT"]:
                body = self.do_request(context, "GET", "given").json()
                del body["_id"]
        elif "base" in data:
            data = data.replace("base_","")
            id = ""
            if request == "PUT":
                id = "123ABC456abc789q"
            body = self.return_usuario()
        elif "update" in data:
            data = data.replace("update_","")
            id = context.given_data.json()["_id"]
            body = self.generate_random_user()
        
        if "invalid" in data:
            data = data.replace("invalid_","")
            if "id" == data:
                id = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(16))

            if data in body:
                body[data] = ""
                
        url = context.base_url + "usuarios/" + id

        if request == "GET":
            response = requests.get(url, headers=context.headers)
        if request == "POST":
            response = requests.post(url, headers=context.headers, json=body)
        if request == "PUT":
            response = requests.put(url, headers=context.headers, json=body)
            if(response.status_code == 200):
                self.nome, self.email, self.password, self.administrador = body["nome"], body["email"], body["password"], body["administrador"] 
        if request == "DEL":
            response = requests.delete(url, headers=context.headers)
                                
        
        return response

    