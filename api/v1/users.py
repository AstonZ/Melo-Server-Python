import leancloud
import model
# from flask import Blueprint
from flask import *
from api.v1.user_info import get_user_info_by_user_id
import comm

bp = Blueprint('users', __name__)


@bp.route('/captcha', methods=['POST'])
def send_capcha():
    params = request.get_json()
    mobile = params.get('mobile')

    if mobile == '13812341234':
        return {'mobile': mobile}

    if len(mobile) != 11:
        raise ValueError(comm.COMM_ARGS_MOBILE_ERROR)

    # request to send sms to user
    leancloud.cloudfunc.request_sms_code(mobile)
    return {'mobile': mobile}


@bp.route('/register', methods=['POST'])
def register():
    """
    @api {post} v1/users/register 新用户注册并登陆

    @apiVersion 1.0.0
    @apiName register

    @apiParam {String} mobile
    @apiParam {String} captcha
    @apiParam {String} password

    @apiSuccess (200) {Dict} userId: leancloud userId

    """

    params = request.get_json()
    mobile = params.get('mobile')
    captcha = params.get('captcha')
    password = params.get('password')
    # leancloud 自带用户指针模型  使用验证码注册
    user = leancloud.User.signup_or_login_with_mobile_phone(mobile, str(captcha))

    is_prd = False
    if is_prd:
        user.refresh_session_token()

    is_first_login = False
    user_info = model.UserInfo.query.equal_to('user', user).find()

    # already exist userinfo
    if len(user_info) > 0:
        user_info = user_info[0]
    else:  # first login user
        is_first_login = True

        # sava user and userInfo
        user_info = model.UserInfo()
        user_info.set_user(user)
        user_info.save()

        user.set('userInfo', user_info)
        user.save()

    if not user_info.get('isPassword', False):
        if password:
            user.set('password', password)
            user_info.set('isPassword', True)
            user_info.save()

    token = leancloud.User.get_current().get_session_token()

    return {
        "token": token,
        "isFirstLogin": is_first_login,
        "userId": user.id,
        "userInfo": get_user_info_by_user_id(user.id, user_info)
    }

