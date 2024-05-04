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
        print(request.form.get('id'))
        print(shopController().getRow(request.form.get('id')))

        shopController().addProduct(shopController().getRow(request.form.get('id')))
    return redirect(url_for('shop.loadShop'))
