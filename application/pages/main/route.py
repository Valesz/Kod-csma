from flask import Blueprint, render_template

main = Blueprint('main', __name__, static_folder='static', template_folder='templates',
                 url_prefix='/main')

@main.get('/')
def loadMain():
    return render_template('main.html')