import leancloud
from flask import *
import comm
import model

bp = Blueprint('user_info', __name__)


def get_user_info_by_user_id(uid, user_info=None):

    if not user_info:
        # fitch user info by uid
        info_list = model.UserInfo.query.equal_to('user', leancloud.User.create_without_data(uid)).find()
        if len(info_list) == 0:
            raise ValueError(comm.USER_INFO_NOT_FOUND)
        user_info = info_list[0]

    nickname = user_info.get_nickname()
    avatar = user_info.get_avatar()
    location = user_info.get_location()
    u_type = user_info.get_type()

    return {
        'nickname': nickname if len(str(nickname)) > 0 else '',
        'avatar': avatar if len(str(avatar)) > 0 is not None else '',
        'location': location if len(str(location)) > 0 is not None else '',
        'type': u_type if len(str(u_type)) > 0 is not None else '',
        'isPassword': user_info.get('isPassword', False)
    }
