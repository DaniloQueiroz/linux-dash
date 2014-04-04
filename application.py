from flask import Flask
from lnx_dash.handlers import dash


app = Flask(__name__)
app.register_blueprint(dash)

if __name__ == '__main__':
    app.run(debug=True)
