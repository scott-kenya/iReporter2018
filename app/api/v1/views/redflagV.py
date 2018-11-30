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