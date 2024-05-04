import json

from flask import Blueprint, render_template, request, redirect, url_for
from .controller import shopController

shop = Blueprint('shop', __name__, static_folder='static', template_folder='templates',
                 url_prefix='/shop')

@shop.get('/')
def loadShop():
    return render_template('shop.html', products=shopController().getAll())

@shop.post('/api/add')
def addProduct():
    if (request.method == "POST"):
        try:
            shopController().addProduct(shopController().getRow(request.form.get('id')))
        except ValueError:
            _msg = json.dumps({
                "code": "",
                "name": "Program Error",
                "description": "Given id not found! Please provide it."
            })
            return redirect(url_for('error.loadError', msg=_msg))
        except FileNotFoundError:
            _msg = json.dumps({
                "code": "",
                "name": "Program Error",
                "description": "Database not found!"
            })
            return redirect(url_for('error.loadError', msg=_msg))
    return redirect(url_for('shop.loadShop'))
