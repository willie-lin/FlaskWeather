#!/usr/bin/python3
# --*-- coding:utf-8 --*--
# @Author    : YuAn
# @Site      :
# @File      : __init__.py.py
# @Time      : 2019/1/09 17:06
# @software  : PyCharm

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, ValidationError
from weather.models import City


class AddCityForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired])
    submit = SubmitField('Add City')

    def validate_city(self, name):
        city_name = City.query.filter_by(name=name.data).first()
        if city_name is not None:
            raise ValidationError('Please use a different city name.')

