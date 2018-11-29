from flask import Flask 
from flask_restplus import Resource, Namespace, fields

from app.api.v1.models.redflagM import redflags
from app.api.v1.models.redflagM import  redflags


incident_namespace = Namespace('Redflag', description='Redflags v1 Endpoint')

flag_model = incident_namespace.model('Redflag',{

                    'id': fields.Integer(required=True),
                    'title': fields.String(required=True),
                    'createdOn': fields.String(required=True),
                    'status': fields.String(required=True),
                    'createdBy': fields.Integer(required=True),
                    'location': fields.String(required=True),
                    'Images': fields.String(required=True),
                    'Videos': fields.String(required=True),
                    'comment': fields.String(required=True),
                    'type': fields.String(required=True)
                 }
                )

flag_update = incident_namespace.model('Redflag Update', {
   'status': fields.String
})


@incident_namespace.route('/redflags')
class Redflag(Resource):

    def get(self):
        return redflags, 200

    @incident_namespace.expect(flag_model)
    def post(self):
        new_flag = incident_namespace.payload
        # new_flag['id'] = len(redflags) + 1
        redflags.append(new_flag)
        return {'output': 'Redflag is added'}, 201

@incident_namespace.route('/redflags/<int:id>')
class Redflags(Resource):

    @incident_namespace.doc()
    def get(self, id):
        for redflag in redflags:
            if redflag['id'] == id:
                return {'redflag': 'Redflag fetched'},200