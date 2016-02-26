# -*- coding: utf-8 -*-
"""User forms."""
from flask_wtf import Form
from wtforms import PasswordField, StringField
from wtforms.validators import DataRequired, Email, EqualTo, Length

from .models import User


class RegisterForm(Form):
    """Register form."""

    username = StringField('Username',
                           validators=[DataRequired(), Length(min=3, max=25)])
    email = StringField('Email',
                        validators=[DataRequired(), Email(), Length(min=6, max=40)])
    password = PasswordField('Password',
                             validators=[DataRequired(), Length(min=6, max=40)])
    confirm = PasswordField('Verify password',
                            [DataRequired(), EqualTo('password', message='Passwords must match')])

    def __init__(self, *args, **kwargs):
        """Create instance."""
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.user = None

    def validate(self):
        """Validate the form."""
        initial_validation = super(RegisterForm, self).validate() 
        if not initial_validation:
            return False
        user = User.query.filter_by(username=self.username.data).first()
        if user:
            self.username.errors.append('Username already registered')
            return False
        user = User.query.filter_by(email=self.email.data).first()
        if user:
            self.email.errors.append('Email already registered')
            return False
        return True



class CreditcardForm(Form):
    """Creditcard form."""

    number = StringField('Credit Card Number',
                           validators=[DataRequired(), Length(min=3, max=25)])
    expiry = StringField('Credit Card Expiration',
                        validators=[DataRequired(), Length(min=2, max=40)])
    cvc = StringField('Credit Card CVC',
                             validators=[DataRequired(), Length(min=2, max=40)])
    address_zip = StringField('Credit Card Zip Code',
                             validators=[DataRequired(), Length(min=2, max=40)])
    address_line1 = StringField('Address Line 1',
                             validators=[DataRequired(), Length(min=2, max=100)])
    address_line2 = StringField('Address Line 2', validators=[])
    address_city = StringField('City',
                             validators=[DataRequired(), Length(min=2, max=40)])
    address_state = StringField('State',
                             validators=[DataRequired(), Length(min=1, max=40)])
    address_country= StringField('Country',
                             validators=[DataRequired(), Length(min=2, max=40)])
    date_of_birth = StringField('Date of Birth',
                             validators=[DataRequired(), Length(min=2, max=40)])
    full_name = StringField('Full Name',
                             validators=[DataRequired(), Length(min=2, max=40)])
    phone = StringField('Phone Number',
                             validators=[DataRequired(), Length(min=2, max=40)])


    def __init__(self, *args, **kwargs):
        """Create instance."""
        super(CreditcardForm, self).__init__(*args, **kwargs)
        self.user = None

    def validate(self):
        """Validate the form."""
        initial_validation = super(CreditcardForm, self).validate()
        if not initial_validation:
            return False

        return True