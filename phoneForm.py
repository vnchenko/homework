from flask_wtf import Form
from wtforms import StringField, SubmitField, DateField, FloatField
from wtforms.validators import DataRequired, AnyOf
from datetime import datetime
from wtforms_components import DateRange


class Phone(Form):

    phone_price = FloatField("price: ")
    phone_vendor = StringField("vendor: ")
    phone_model = StringField("model: ", validators=[DataRequired(), AnyOf(values=['LG', 'ASUS', 'NOKIA'])])
    phone_date = DateField("date: ", format='%m/%d/%Y', validators=[DateRange(min=datetime(2000, 1, 1))])

    submit = SubmitField("Save")
