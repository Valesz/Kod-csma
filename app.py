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

app.register_blueprint(main)
app.register_blueprint(shop)
app.register_blueprint(error)
app.register_blueprint(cart)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route('/')
def hello_world():  # put application's code here
    return redirect(url_for('main.loadMain'))

@app.errorhandler(HTTPException)
def errorHTTP(e):
    _error = json.dumps({
        "code": e.code,
        "name": e.name,
        "description": e.description
    })
    return redirect(url_for('error.loadError', msg=_error))

if __name__ == '__main__':
    app.run(debug=True)
