from flask import Blueprint, render_template, request

error = Blueprint('error', __name__, static_folder='static', template_folder='templates',
                  url_prefix='/error')

@error.route('/')
def loadError():
    return render_template('error.html', message=request.args.get('msg'))