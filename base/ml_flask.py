from flask import Flask, Response, jsonify

""" 封装返回格式以 result字段装载response,json返回 可以用flask_restful取代 """
class MLResponse(Response):
    @classmethod
    def force_type(cls, rv, environ=None):
        if isinstance(rv, (dict, list)):
            if 'result' not in rv:
                rv={'result':rv}
            rv=jsonify(rv)
        return super(MLResponse, cls).force_type(rv, environ)

class MLFlask(Flask):
    response_class=MLResponse