
import base

from api.v1 import *

import leancloud
# from config import LC_AppID, LC_MasterKey
from leancloud import logging

is_prd = False

app = base.MLFlask(__name__)

leancloud.init(app_id='DXY29E1Fr9hDeubTIrrskf7m-gzGzoHsz', master_key='BCQikimy4Dwu4Odpy3Nbk8Dc')
logging.basicConfig(level=logging.DEBUG)

# register blueprint
app.register_blueprint(users.bp, url_prefix='/v1/users')
app.register_blueprint(upload.bp, url_prefix='/v1/upload')


@app.route('/index')
def index():
    return {'data': 'indexPage'}


@app.route('/test')
def test_obj():

    return {'data': 'done!'}
    

if __name__ == '__main__':
    app.run(debug=True)
