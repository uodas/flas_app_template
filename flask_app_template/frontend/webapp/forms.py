"""
Web Forms
"""
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Length, InputRequired, NumberRange
from wtforms.fields.simple import HiddenField

class AppTemplateForm(FlaskForm):
    """The class represents the web form.
    
    """
    text = StringField('Some text:', validators=[DataRequired(), Length(max=20)])
    number = IntegerField('Some number:', validators=[InputRequired(), NumberRange(min=0, max=5)])
    hidden = HiddenField()
    submit =  SubmitField('Submit')

    