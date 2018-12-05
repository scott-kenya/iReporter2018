from flask import Flask 
from flask_restplus import Namespace, fields, reqparse

from .verification import Verification

incidents = []

incident_namespace = Namespace('Incident', description='Incidents v1 Endpoint')

incident_model = incident_namespace.model('Incident',{

                    'id': fields.Integer(required=True),
                    'Title': fields.String(required=True),
                    'createdOn': fields.String(required=True),
                    'status': fields.String(required=True),
                    'createdBy': fields.Integer(required=True),
                    'location': fields.String(required=True),
                    'Images': fields.Float(required=True),
                    'Videos': fields.String(required=True),
                    'comment': fields.String(required=True),
                    'type': fields.String(required=True)
                 }
          		)



incident_update = incident_namespace.model('Incident Update', {
   'status': fields.String
})



parser = reqparse.RequestParser(bundle_errors=True)
parser.add_argument('type',
                    type=str,
                    required=True,
                    choices=("redflag", "intervention"),
                    help="This field cannot be left blank or Bad choice: {error_msg}"
                    )

parser.add_argument('location',
                    type=str,
                    required=True,
                    location='json',
                    help="This field cannot be left blank or Bad choice: {error_msg}"
                    )

parser.add_argument('Title',
                    type=str,
                    required=True,
                    location='json',
                    help="This field cannot be left blank or Bad choice: {error_msg}"
                    )


parser.add_argument('status',
                    type=str,
                    required=True,
                    location='json',
                    help="This field cannot be left blank or Bad choice: {error_msg}"
                    )


parser.add_argument('comment',
                    type=str,
                    required=True,
                    location='json',
                    help="This field cannot be left blank or Bad choice: {error_msg}"
                    )


parser.add_argument('Videos',
                    type=str,
                    required=True,
                    location='json',
                    help="This field cannot be left blank or Bad choice: {error_msg}"
                    )


parser.add_argument('Images',
                    type=str,
                    required=True,
                    location='json',
                    help="This field cannot be left blank or Bad choice: {error_msg}"
                    )