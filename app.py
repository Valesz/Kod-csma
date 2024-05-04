from flask import Flask
from flask import redirect
from application.main.route import main
from application.shop.route import shop
from flask_session import Session

app = Flask(__name__)

app.register_blueprint(main)
app.register_blueprint(shop)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route('/')
def hello_world():  # put application's code here
    return redirect(main.url_prefix)


if __name__ == '__main__':
    app.run(debug=True)
