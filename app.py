from flask import Flask
from flask import render_template, redirect
from application.main.route import main
from application.shop.route import shop

app = Flask(__name__)

app.register_blueprint(main)
app.register_blueprint(shop)

@app.route('/')
def hello_world():  # put application's code here
    return redirect(main.url_prefix)


if __name__ == '__main__':
    app.run(debug=True)
