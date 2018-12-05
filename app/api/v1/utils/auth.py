import jwt

from functools import wraps
from flask import request




def token_required(function):
    '''creating a token'''
    @wraps(function)
    def decorated(*args, **kwargs):
        token = None
        current_user = None
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
        if not token:
            return {"output": "the access token is missing, Login"}, 401
        try:
            data = jwt.decode(token, Config.SECRET_KEY)
            for user in users:
                if user['email'] == data['email']:
                    current_user = user

        except:

            print(Config.SECRET_KEY)
            return {"output": "This token is invalid"}, 403

        return function(current_user, *args, **kwargs)
    return decorated