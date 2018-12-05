from flask import Flask 
from flask_restplus import Resource, Namespace, fields,reqparse

from app.api.v1.models.incidentsM import incidents, incident_namespace, incident_model, incident_update, parser
from app.api.v1.utils.auth import token_required




@incident_namespace.route('/incidents')
class Incident(Resource):
    #@token_required
    def get(self):
        return incidents, 200

    @incident_namespace.expect(incident_model)
    #@token_required
    def post(self):
        args = parser.parse_args()
        new_flag = incident_namespace.payload
        new_flag['id'] = len(incidents) + 1
        incidents.append(new_flag)
        return {'output': 'Incident is added', 'data': [new_flag]}, 201




@incident_namespace.route('/incidents/<int:id>')
class Incidents(Resource):

    @incident_namespace.doc()
    #@token_required
    def get(self, id):
        for incident in incidents:
            if incident['id'] == id:
                return {'output': 'Incident fetched'},200

    @incident_namespace.expect(incident_update)
    #@token_required
    def put(self, id):
        up = incident_namespace.payload
        for incident in incidents:
             if incident['id'] == id:
                 incident.update(up)
                 return {"output":"Incident updated"}, 201
    #@token_required
    def delete(self, id):
        for incident in incidents:
            if incident['id'] == id:
                incidents.remove(incident)
                return {"output": "Incident Deleted"},  204

