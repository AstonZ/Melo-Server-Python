import leancloud
from flask import *
import comm
import model
from xpinyin import Pinyin

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


@bp.route('/<uid>', methods=['PUT'])
@comm.login_required
def set_user_info(uid):
    """
    @api {PUT} v1/users/<uid> 修改用户信息
    @apiVersion v1.0.0
    @apiName setUserInfo
    @apiGroup UserInfo
    @apiPermission self
    ['user', 'nickname', 'avatar', 'location', 'type'
    @apiParam (optional) {String} nickname
    @apiParam (optional) {String} avatarId
    @apiParam (optional) {String} location
    @apiParam (optional) {String} type
    # @apiParam (optional) {String} nickname
    # @apiParam (optional) {String} nickname
    """

    # user self can modify info
    if leancloud.User.get_current().id != uid:
        raise ValueError(comm.USER_PERMISSION_DENIED)
    user = leancloud.User.create_without_data(uid)
    info_list = model.UserInfo.query.equal_to('user', user).find()
    if len(info_list) == 0:
        raise ValueError(comm.USER_INFO_NOT_FOUND)
    user_info = info_list[0]
    params = request.get_json()
    nickname = params.get('nickname')
    avatarId = params.get('avatarId')

    rv = {
        'userId': user.id
    }

    p_transfer = Pinyin()
    if nickname:
        rv["nickname"] = nickname
        py_nickname = p_transfer.get_pinyin(nickname, '')
        if py_nickname:
            user_info.set('py_nickname', py_nickname)
            rv['pyNickname'] = py_nickname if len(py_nickname) > 0 else 'z'

    if avatarId:
        ava_list = leancloud.File.query.equal_to('objectId', avatarId).find()
        if len(ava_list) > 0:
            avatar = ava_list[0]
            rv["avatar"] = avatar.url
            user_info.set_avatar(avatar)

    user_info.save()
    return rv
