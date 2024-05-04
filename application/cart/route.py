import json

from flask import Blueprint, render_template, request, redirect, url_for
from .controller import cartController

cart = Blueprint('cart', __name__, static_folder='static', template_folder='templates',
                 url_prefix='/cart')

@cart.get('/')
def loadCart():
    return render_template('cart.html', items=cartController().getAll(),
                           costs=cartController().gerCartValues())

@cart.post('/api/remove')
def removeItem():
    try:
        cartController().removeItem(request.form.get('id'))
    except ValueError:
        _msg = json.dumps({
            "code": "",
            "name": "Program Error",
            "description": "Given id not found! Please provide it."
        })
        return redirect(url_for('error.loadError', msg=_msg))
    return redirect(url_for('cart.loadCart'))

@cart.post('/api/add')
def incrementItem():
    try:
        cartController().addItem(request.form.get('id'))
    except ValueError:
        _msg = json.dumps({
            "code": "",
            "name": "Program Error",
            "description": "Given id not found! Please provide it."
        })
        return redirect(url_for('error.loadError', msg=_msg))
    return redirect(url_for('cart.loadCart'))

@cart.post('/api/removeAll')
def removeItemAll():
    cartController().removeAll()
    return redirect(url_for('cart.loadCart'))

@cart.post('/api/buy')
def buyItems():
    cartController().removeAll()
    return redirect('http://www.eotvos.u-szeged.hu/sites/default/files/muhelyek/adrienne182/EKA_k%C3%B6sz%C3%B6nj%C3%BCk_2021.jpg')
