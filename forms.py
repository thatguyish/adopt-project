from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField,SelectField,BooleanField
from wtforms.validators import URL,Optional,NumberRange,Required

class PetForm(FlaskForm):
    """A form representing a pet"""

    name = StringField('Pet Name')

    species = SelectField('Pet Species',choices=[('cat','Cat'),('dog','Dog'),('porcupine','Porcupine')])

    photo_url = StringField('Pet Photo',validators=[URL(),Optional()])

    age = IntegerField('Pet Age',validators=[NumberRange(min=0,max=30),Optional()])

    notes = StringField('Pet Notes')

    available = BooleanField('Available')