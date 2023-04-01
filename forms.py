from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, IntegerField, TimeField, SelectMultipleField
from wtforms.validators import DataRequired, Length, NumberRange


class DataForm(FlaskForm):
    gender_choices = [('male', 'Male'), ('female', 'Female'), ('other', 'Other')]
    gender = SelectField('Gender', choices=gender_choices, validators=[DataRequired()])

    age = IntegerField('Age', validators=[DataRequired(), NumberRange(min=1)])

    day = IntegerField('Day', validators=[DataRequired(), NumberRange(min=1, max=31)])

    time = TimeField('Time', validators=[DataRequired()])

    interest_choices = [('sports', 'Sports'), ('music', 'Music'), ('entertainment', 'Entertainment'), ('books', 'Books'),
                        ('shopping', 'Shopping'), ('food and drinks', 'Food and Drinks')]
    interests = SelectMultipleField('Interests', choices=interest_choices, validators=[DataRequired()])

    postal_code = StringField('Postal Code', validators=[DataRequired(), Length(min=1, max=10)])

    min_budget = IntegerField('Minimum Price Level', validators=[NumberRange(min=0, max=4)],
                              render_kw={"placeholder": "0 for lowest price"})
    max_budget = IntegerField('Maximum Price Level', validators=[NumberRange(min=0, max=4)],
                              render_kw={"placeholder": "4 for highest price"})
    submit = SubmitField('Submit')

    def validate(self, **kwargs):
        # Run the default validations
        if not super(DataForm, self).validate():
            return False

        # Custom validation: min budget should be lower than max budget
        if self.min_budget.data and self.max_budget.data and self.min_budget.data >= self.max_budget.data:
            self.min_budget.errors.append("Minimum budget must be lower than maximum budget.")
            return False

        return True
