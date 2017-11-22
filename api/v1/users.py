import leancloud
from flask import *
import model

bp=BluePrint('users', __name__)

@app.route('/captcha', methods=['POST'])
def send_capcha():
    """
    """
    params=request.get_json()
    mobile=params.get('mobile')
    return {'mobile':mobile}
