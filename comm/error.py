COMM_ERROR = 10000, '系统错误'

COMM_ARGS_ERROR = 10100, '参数错误'
COMM_ARGS_MOBILE_ERROR = 10101, '手机号格式错误'
COMM_ARGS_OBJECT_EXISTS = 10102, '数据已存在'
COMM_ARGS_CAPTCHA_ERROR = 10103, '验证码发送失败'
COMM_ARGS_EXT_LOGIN_ERROR = 10104, '三方平台仅支持weibo/weixin/qq'
COMM_ARGS_NOT_IN_LIST = 10200, '参数超出允许的范围'
COMM_ARGS_NOT_ILLEGAL_STRINGS = 10201, '汉字转拼音失败'
COMM_ARGS_MSG_NOT_FOUND = 10202, '无效的短信验证码'

USER_ALREADY_EXISTS = 20001, '用户已存在'
USER_NOT_EXIST = 20002, '用户不存在'
USER_NOT_REGISTER = 20003, '该账号未注册'
USER_UNAUTHORIZED = 20100, '用户未登录'
USER_PERMISSION_DENIED = 20101, '用户权限不足'
USER_WITHOUT_GROUP = 20102, '用户未加入班级'
USER_HAS_PASSWORD = 20103, '首次设置密码失败。用户已设置了密码，如需更改，请到用户中心中更改密码'
USER_PASSWORD_TOO_SHORT = 20104, '密码过短，请设置六位及以上密码'
USER_INFO_NOT_FOUND = 20203, '未查询到有效的用户信息'

TASK_HOMEWORK_ALREADY_EXIST = 30000, '作业已提交，请勿重复提交'
TASK_NOT_FOUND = 30001, '未查询到有效的任务'
TASK_HOMEWORK_NOT_FOUND = 30002, '未查询到有效的作业数据'
TASK_TYPE_ERROR = 30003, '作业类型错误'
TASK_DUN_ERROR_TIME_LIMIT = 30004, '催收作业间隔过短'

MESSAGE_NOT_FOUND_OR_ALREADY_DISPOSE = 40001, '未查询到有效的申请信息或申请已被处理'
GROUP_NOT_FOUND = 40002, '未查询到有效的班级信息'
GROUP_NOT_FOUND_USER = 40003, '班级中不包含自己'
EVALUATION_NOT_FOUND = 40004, '未查询到有效的评测信息'
COMMENT_NOT_FOUND = 40005, '请先设置一键评语内容。'

COURSE_NOT_PAID = 40101, '课程未购买'
COURSE_NOT_FOUND = 40102, '未查询到有效的课程'

CDKEY_NOT_FOUND = 40200, '查无此卡'
CDKEY_NOT_MATCHING = 40201, '激活卡与安全码不匹配'
CDKEY_USED = 40202, '激活卡已激活，如不是本人激活，请咨询客服'

LEANCLOUD_ERRORS = {
    60127: '手机号格式错误',
    60210: '手机号和密码不匹配',
    60211: '手机号和密码不匹配',
    60219: '登录失败次数超过限制，请稍候再试，或者通过忘记密码重设密码',
    60429: '请求过多，请稍后重试',
    60430: '流控限制，每分钟最多上传30个文件，请稍后重试',
    60502: '服务器维护中',
    60601: '发送短信过于频繁，请稍后再试',
    60602: '发送短信失败，请稍后再试',
    60603: '无效的短信验证码'
}
