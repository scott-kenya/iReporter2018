import jwt

from functools import wraps
from flask import request



def token_required(f):
	@wraps(f)
	def decorated(*arg,**kwargs):
		token = None
		if 'X-API-KEY' in request.headers:
			token = request.headers['X-API-KEY']
		if not token:
			return {'output': 'token is missing'},401
		try:
			token = jwt.decode(token,'qazxswedc',algorithms=['HS256'])
		except:
			return {'output': 'token is invalid'},401
		return f(*arg,**kwargs)
	return decorated

