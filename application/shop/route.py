from flask import Blueprint, render_template

shop = Blueprint('shop', __name__, static_folder='static', template_folder='templates',
                 url_prefix='/shop')

@shop.get('/')
def loadShop():
    return render_template('shop.html')