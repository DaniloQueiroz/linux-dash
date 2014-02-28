from flask import Flask
from flask.templating import render_template
from linux_info import linux_info_api

app = Flask(__name__)
app.register_blueprint(linux_info_api, url_prefix='/api')


@app.route('/')
def dashboard():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
