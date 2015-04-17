from app import app
import flask


@app.route('/')
@app.route('/index')
def index():
    return flask.render_template('index.html', title='Home')
