import json

from flask import Blueprint, render_template, request

error = Blueprint('error', __name__, static_folder='static', template_folder='templates',
                  url_prefix='/error')


@error.route('/')
def loadError():
    _msg = json.loads(request.args.get('msg'))
    return render_template('error.html', msg=_msg)
