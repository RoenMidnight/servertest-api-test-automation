from jwt import JWT

def before_all(context):
    context.base_url = "https://serverest.dev/"
    context.bearer_token = ""    
    context.headers = {
        "Authorization": f"Bearer {context.bearer_token}"
    }

def after_scenario(context, step):
    if context.bearer_token == "":
        jwt = JWT()
        jwt.generate_jwt(context)