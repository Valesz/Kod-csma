import json

from flask import Blueprint, render_template, request, redirect, url_for
from .controller import cartController

cart = Blueprint('cart', __name__, static_folder='static', template_folder='templates',
                 url_prefix='/cart')


@cart.get('/')
def loadCart():
    """ Loads the cart page.

    Gives the following attributes to the rendered html:
        items: all the products in the user's cart represented as a list of products.

    """

    return render_template('cart.html', items=cartController().getAll(),
                           costs=cartController().gerCartValues())


@cart.post('/api/remove')
def removeItem():
    """ Removes the given item from the user's cart.

    :except: ValueError: redirects to the error page and attaches the msg error message.

    :return: Redirection to the cart page.
    """

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
    """ Adds the given item to the cart of the user.

    :parameter id: The id of the product to add to the cart. Gets it from a form.

    :except: ValueError: redirects to the error page and attaches the msg error message.

    :return: Redirection to the cart page.
    """

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
    """ Empties the cart of the user

    :return: Redirection to the cart page.
    """

    cartController().removeAll()
    return redirect(url_for('cart.loadCart'))


@cart.post('/api/buy')
def buyItems():
    """ Empties the cart of the user

    :return: Redirects to the best place to donate 1% of your tax to ;)
    """
    cartController().removeAll()
    return redirect(
        'http://www.eotvos.u-szeged.hu/sites/default/files/muhelyek/adrienne182/EKA_k%C3%B6sz%C3%B6nj%C3%BCk_2021.jpg')
