from flask import Flask 
from flask_restplus import Namespace, fields


redflags = []

# incident_namespace = Namespace('Redflag', description='Redflags v1 Endpoint')

# flag_model = incident_namespace.model('Redflag',{

#                     'id': fields.Integer(required=True),
#                     'title': fields.String(required=True),
#                     'createdOn': fields.String(required=True),
#                     'status': fields.String(required=True),
#                     'createdBy': fields.Integer(required=True),
#                     'location': fields.String(required=True),
#                     'Images': fields.Float(required=True),
#                     'Videos': fields.String(required=True),
#                     'comment': fields.String(required=True),
#                     'type': fields.String(required=True)
#                  }
#           		)



# flag_update = incident_namespace.model('Redflag Update', {
#    'status': fields.String
# })
