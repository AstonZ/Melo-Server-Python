import os
import sys

import flask
from flask.ext.restful import Api, Resource
import base

from api.v1 import *

import leancloud
# from config import LC_AppID, LC_MasterKey
from leancloud import logging
import model

is_prd = False

app = base.MLFlask(__name__)
api = Api(app)

leancloud.init('DXY29E1Fr9hDeubTIrrskf7m','BCQikimy4Dwu4Odpy3Nbk8Dc')
logging.basicConfig(level=logging.DEBUG)

# register blueprint
app.register_blueprint(users.bp, url_prefix='/v1/users')

@app.route('/index')
def index():
    return {'data':'indexPage'}

@app.route('/test')
def testObj():
    testUser=model.UserInfo()
    testUser.set_nickname='jack'
    testUser.set_
    return {'data':'done!'}
    

if __name__ == '__main__':
    app.run(debug=True)
