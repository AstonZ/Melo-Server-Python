import os
import sys

import flask
from flask.ext.restful import Api, Resource
import leancloud
 
is_prd=False

app=Flask(__name__)
api=Api(app)

# register blueprint
class IndexAPI(Resource):
    def get(self):
        return {'msg':'Server OK!'}


