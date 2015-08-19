from wtforms import StringField
from wtforms import Form
from wtforms.ext.appengine.db import model_form
from wtforms.validators import DataRequired

class AForm(Form):
    name = StringField("Example Name", validators=[DataRequired()])
