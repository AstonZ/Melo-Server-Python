import os
import sys

import flask
from flask.ext.restful import Api, Resource
import base

import leancloud
# from config import LC_AppID, LC_MasterKey
from leancloud import logging

is_prd = False

app = base.MLFlask(__name__)
api = Api(app)

leancloud.init('DXY29E1Fr9hDeubTIrrskf7m','BCQikimy4Dwu4Odpy3Nbk8Dc')
logging.basicConfig(level=logging.DEBUG)

# register blueprint

@app.route('/index')
def index():
    return {'data':'indexPage'}

@app.route('/test')
def testObj():
    test_object=leancloud.Object.extend('TestObject')
    test_object=TestObject()
    test_object.set('words','Hi, Done!')
    test_object.save()
    return {'data':'done!'}
    

if __name__ == '__main__':
    app.run(debug=True)
