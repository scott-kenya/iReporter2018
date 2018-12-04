from flask import Flask 
from flask_restplus import Namespace, fields

from .verification import Verification

incidents = []

incident_namespace = Namespace('Incident', description='Incidents v1 Endpoint')

incident_model = incident_namespace.model('Incident',{

                    'id': fields.Integer(required=True),
                    'title': fields.String(required=True),
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



class Incidents(Verification):
  def __init__(self,items):
    self.items = items

  def check_incident_post(self):
    input=self.is_incident_payload(self.items) 
    strings = [self.items['title'],self.items['type']]
    keys = ['title', 'type']
    if input is False:
      return {'output':'invalid input'},406
    elif self.is_empty(strings) is not False:
      return {'output': 'data set {} is empty'.format(keys[self.is_empty(strings)])},406
    elif self.is_whitespace(strings) is not False:
      return {'output': 'data set {} contains only white space'.format(keys[self.is_whitespace(strings)])},406
    else:
      return 1

  def add_incident(self):
    self.items['id'] = len(incidents)
    for incident in incidents:
      if incident['title'] == self.items['title']:
        return {'output': 'An incident has be added'},201
    incidents.append(self.items)
    return {'output': 'product has added to database'},201

  @classmethod
  def get_all_incident_records(cls):
    if len(incidents) == 0:
      return {'output': 'no incidents found'},404
    else:
      return [{'message': 'all incidents'},incidents],200

  @classmethod
  def get_one_incident(cls, id):
    if len(incidents) == 0:
      return {'output': 'no incidents found'},404
    else:
      return incidents[id],200