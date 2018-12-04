import jwt
from flask import request

from .verification import Verification

user_accounts = [{'id':'0','fname': 'scott', 'lname': 'francis','othernames':'admin','email': 'scott@gmail.com','password': '1234','username':'admin','isAdmin':'True','phoneNumber':'123456789'}]


class UserAccounts(Verification):
	"""
	class for user accounts
	"""
	def __init__(self,items):
		self.items = items
		# self.payload = user_accounts

	def check_user_input(self):
		strings = [self.items['email'],self.items['password']]
		keys = ['email','password']
		payload=self.is_login_payload(self.items) 
		if payload is False:
			res = {'output':'invalid payload'},406
		elif self.is_empty(strings) is not False:
			res = {'output': 'data set {} is empty'.format(keys[self.is_empty(strings)])},406
		elif self.is_whitespace(strings) is not False:
			res = {'output': 'data set {} contains only white space'.format(keys[self.is_whitespace(strings)])},406
		elif self.is_email(self.items['email']) is True:
			res = {'output': 'invalid email'}, 406
		else:
			res = 1
		return res

	def login(self):
		for user_account in user_accounts:
			if user_account.get('email') == self.items['email']:
				token = jwt.encode({'id':user_account['id']},'qazxswedc',algorithm='HS256').decode('UTF-8')
				return [{'message': 'Login successful'},{'token':token}]
		return {'output': 'email or password invalid'},406


	def check_register_input(self):
		strings = [self.items['fname'],self.items['lname'],self.items['othernames'],
		self.items['email'],self.items['phoneNumber'],self.items['password'],self.items['isAdmin'],self.items['username']]
		keys = ['first name', 'last_name', 'othernames', 'email', 'password','username','isAdmin']
		payload = self.is_register_payload(self.items)
		if payload is False:
			return {'output':'invalid payload'},406
		elif self.is_whitespace(strings) is not False:
			return {'result': 'data set {} contains only white space'.format(keys[self.is_whitespace(strings)])},406
		elif self.is_empty(strings) is not False:
			return {'output': 'data set {} is empty'.format(keys[self.is_empty(strings)])}
		elif self.is_email(self.items['email']) is True:
			return {'output': 'invalid email'}, 406
		elif self.items['username'] != 'admin' and self.items['username'] != 'new_user':
			return {'output': 'invalid role'}, 406
		else:
			self.items['id'] = len(user_accounts)
			user_accounts.append(self.items)
			return 1

	@classmethod
	def get_id(cls):
		token = request.headers['X-API-KEY']
		userId = token = jwt.decode(token,'qazxswedc',algorithms=['HS256']),401
		return userId
