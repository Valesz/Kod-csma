import json

from flask import Flask
from flask import redirect, url_for
from application.main.route import main
from application.shop.route import shop
from application.error.route import error
from application.cart.route import cart
from flask_session import Session
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

# Registers the blueprints to the app's blueprint.
app.register_blueprint(main)
app.register_blueprint(shop)
app.register_blueprint(error)
app.register_blueprint(cart)

# Set's the session config
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


@app.route('/')
def loadApp():  # put application's code here
    """ Redirects to the main page.

    :return: Redirects to the main page.
    """
    return redirect(url_for('main.loadMain'))


@app.errorhandler(HTTPException)
def errorHTTP(e):
    """ Handles the basic HTTP errors.

    :param e: The HTTP exception object.
    :return: Redirection to the error page with the msg argument.
    """
    _error = json.dumps({
        "code": e.code,
        "name": e.name,
        "description": e.description
    })
    return redirect(url_for('error.loadError', msg=_error))


if __name__ == '__main__':
    # The mother of all functions!

    app.run(debug=True)
