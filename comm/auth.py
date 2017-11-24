from functools import wraps
import flask
# import model
import comm
import leancloud


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        # login status
        is_login_flag = False
        token = flask.request.headers.get('token')
        if token:
            try:
                user = leancloud.User.become(token)
            except leancloud.LeanCloudError:
                user = None
            if user:
                leancloud.User.set_current(user)
                is_login_flag = True
        elif is_login(leancloud.User.get_current()):
            is_login_flag = True

        if not is_login_flag:
            raise ValueError(comm.USER_UNAUTHORIZED)

        resp = f(*args, **kwargs)
        return resp
    return decorated_function


def is_login(user):
    if user is not None:
        if user.is_authenticated():
            return True
    return False
