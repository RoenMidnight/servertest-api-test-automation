import requests
from faker import Faker
import random, string

class JWT:
    def generate_random_user(self):
        fake = Faker()
        nome = fake.name()
        email = nome.replace(" ", "_") + "@qa.com.br"
        for _ in range(5):
            password = fake.password(length=16)
        administrador = random.choice(["true", "false"])

        return {"nome": nome, "email": email, "password": password, "administrador": administrador}
    
    def generate_jwt(self, context):
        new_user = self.generate_random_user()

        requests.post(context.base_url + "usuarios", headers=context.headers, json=new_user)
        context.bearer_token = requests.post(context.base_url + "login", headers=context.headers, json={
            "email": new_user["email"],
            "password": new_user["password"]
        }).json()["authorization"]