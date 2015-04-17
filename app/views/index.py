from app import app
import flask
from flask.ext.wtf import Form
from wtforms import StringField
from wtforms.validators import DataRequired


@app.route('/', methods=['GET', 'POST'])
def index():
    form = HootputtForm()

    if form.validate_on_submit():
        print 'It worked! name: %s, strokes: %s' % (form.name.data, form.strokes.data)

    return flask.render_template('index.html',
      title='Hootputt',
      form=form)

class HootputtForm(Form):
    name = StringField('name', validators=[DataRequired()])
    strokes = StringField('strokes', validators=[DataRequired()])
