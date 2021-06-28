# Author Joey Whelan

import os
from flask import request, Flask, abort
from flask_restful import Resource, Api, reqparse
from main.services import cleaner

class CleanerApi(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('document', required=True, location='json', help='Invalid document')
        args = parser.parse_args() 
        tokens = cleaner.clean(args.document)
        return {'tokens': tokens}, 200

def create_app():
    app = Flask(__name__.split('.')[0])
    api = Api(app)
    api.add_resource(CleanerApi,'/')
    return app