from functools import wraps
import os

from flask import make_response, request

try:
    from dotenv import load_dotenv
    load_dotenv()
except:
    print('no .env file, using external enviromental variable')

Username = os.environ['EVERYONES_USERNAME']
Password = os.environ['EVERYONES_PASSWORD']

def auth_required(f):
    @wraps(f)
    def deocrated(*args, **kwargs):
        auth = request.authorization
        if auth and auth.username == Username and auth.password == Password:
            return f(*args, **kwargs)
        return make_response('<h1>Invalid login!</h1>',401,{'WWW-authenticate': 'Basic reald="Login required!"'})
    
    return deocrated