from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class PokemonFinderForm(FlaskForm):
    name = StringField("Pokemon Name", validators = [DataRequired()])
    submit = SubmitField()
