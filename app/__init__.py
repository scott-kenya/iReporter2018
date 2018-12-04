from flask import Flask, Blueprint
from flask_restplus import Api, Resource

from app.api.v1.views.incidentsV import incident_namespace



def create_app():

    app = Flask(__name__)
    api = Api(app, title="iReporter", version="1.0",
          description=' iReporter api version 1')
    
   
    api.add_namespace(incident_namespace, path='/api/v1')

    
    return app












