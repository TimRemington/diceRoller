from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField, SelectField, BooleanField
from wtforms.validators import DataRequired

class DiceRoller(FlaskForm):
    trials = IntegerField('Number of Trials', validators=[DataRequired()])
    rules = SelectField('X-Again Rule', choices=[('10', '10-Again'), ('9', '9-Again'), ('8', '8-Again'), ('11', 'Force 1'), ('1', 'Infinite 8-Again')])
    amount = IntegerField('Amount of Dice', validators=[DataRequired()])
    submit = SubmitField('Roll Em')
