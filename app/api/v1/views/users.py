from flask import Flask,request
from flask_restplus import Resource, Namespace,fields

from app.api.v1.utils.auth import token_required
from app.api.v1.models.users import UserAccounts,user_accounts

users ={}

users_namespace = Namespace('users',description='Users v1 Endpoints')

model_login = users_namespace.model('users model',{
	'email':fields.String('scott@gmail.com'),
	'password':fields.String('1234')
	})

model_register = users_namespace.model('register new_user',{
	'fname':fields.String('new_user\'s first name'),
	'lname': fields.String('new_user\'s last name'),
	'email': fields.String('new_user\'s email'),
	'othernames': fields.String('new_user\'s othernames'),
	'password': fields.String('new_user\'s password'),
	'isAdmin': fields.String('new_user\'s isAdmin'),
	'phoneNumber': fields.String('new_user\'s phoneNumber'),
	'username' : fields.String('new_user\'s username')
	})

@users_namespace.route('/login')
class Login(Resource):
	@users_namespace.expect(model_login,validate=True)
	def post(self):
		obj = UserAccounts(request.get_json())
		if obj.check_user_input() == 1:
			return obj.login()
		else:
			return obj.check_user_input()


@users_namespace.route('/register')
class RegisterUser(Resource):
	@token_required
	@users_namespace.doc(security='apikey')
	@users_namespace.expect(model_register,validate=True)
	def post(self):
		data = request.get_json()
		obj = UserAccounts(data)
		if obj.check_register_input() == 1:
			return [{'output': 'new user added'},data]
		else:
			return obj.check_register_input()