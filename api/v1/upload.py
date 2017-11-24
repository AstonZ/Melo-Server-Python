import leancloud
from flask import *
import comm


bp = Blueprint('upload', __name__)


@bp.route('/uploadImg', methods=['POST'])
@comm.login_required
def upload_file():
    uploader = request.files['file']
    file = leancloud.File(uploader.filename, data=uploader.stream)
    file.save()
    return {
        'fileId': file.id,
        'url': file.url
    }
