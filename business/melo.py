from sqlite3 import dbapi2 as sqlite3
from flask import Flask, Blueprint, request, session, g, redirect, url_for, abort, \
     render_template, flash, current_app, jsonify
from werkzeug.wrappers import Response
    

# import env_settings

app=Flask(__name__)

# define json reponse class
class JsonResponse(Response):
  default_mimetype='application/json'

@classmethod
def force_type(cls,response,environ=None):
  # if isinstance(response,dict):
    # response=jsonify(response)
  return super(JsonResponse,cls).force_type(response,environ)

app.response_class=JsonResponse

# load settings from moudle
# app.config.from_object('env_settings')

@app.route('/about/')
def about():
  return {'message':'about page'}

if __name__=='__main__':
  app.run(debug=True)
