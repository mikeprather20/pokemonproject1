from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo

class EditProfile(FlaskForm):
    first_name = StringField('First Name', validators = [])
    last_name = StringField('Last Name', validators = [])
    email = StringField('Email', validators = [])
    submit = SubmitField()