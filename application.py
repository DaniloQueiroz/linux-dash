from flask import Flask, abort
from flask.templating import render_template
from util import as_json, to_underscore, get_info_function


app = Flask(__name__)


@app.route('/')
def dashboard():
    return render_template('index.html')


@app.route('/api/<info_name>')
@as_json
def api_call(info_name):
    info_name = to_underscore(info_name)

    fn = get_info_function(info_name)
    if fn:
        return fn()
    else:
        abort(404)


if __name__ == '__main__':
    app.run(debug=True)
