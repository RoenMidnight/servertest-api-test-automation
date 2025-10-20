import requests

def create_new_obj(context, object, data):
    url = context.base_url + object
    context.given_data  = requests.post(url, headers=context.headers, json=data)