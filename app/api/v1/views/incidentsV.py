from flask import Flask 
from flask_restplus import Resource, Namespace, fields

from app.api.v1.models.incidentsM import incidents
from app.api.v1.models.incidentsM import  incidents

from app.api.v1.models.incidentsM import incidents, incident_namespace, flag_model, flag_update



@incident_namespace.route('/incidents')
class Incident(Resource):

    def get(self):
        return incidents, 200

    @incident_namespace.expect(flag_model)
    def post(self):
        new_flag = incident_namespace.payload
        # new_flag['id'] = len(incidents) + 1
        incidents.append(new_flag)
        return {'output': 'Incident is added'}, 201

@incident_namespace.route('/incidents/<int:id>')
class Incidents(Resource):

    @incident_namespace.doc()
    def get(self, id):
        for incidents in incidents:
            if incidents['id'] == id:
                return {'incidents': 'Incident fetched'},200

    @incident_namespace.expect(flag_update)
    def put(self, id):
        up = incident_namespace.payload
        for incidents in incidents:
             if incidents['id'] == id:
                 incidents.update(up)
                 return {"message":"Incident updated"}, 201

    def delete(self, id):
        for incident in incidents:
            if incident['id'] == id:
                incidents.remove(incident)
                return {'Message': 'ncident Deleted'},  204

