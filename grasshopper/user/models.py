# -*- coding: utf-8 -*-
"""User models."""
import datetime as dt

from flask_login import UserMixin

from grasshopper.database import Column, Model, SurrogatePK, db, reference_col, relationship
from grasshopper.extensions import bcrypt


class Role(SurrogatePK, Model):
    """A role for a user."""

    __tablename__ = 'roles'
    name = Column(db.String(80), unique=True, nullable=False)
    user_id = reference_col('users', nullable=True)
    user = relationship('User', backref='roles')

    def __init__(self, name, **kwargs):
        """Create instance."""
        db.Model.__init__(self, name=name, **kwargs)

    def __repr__(self):
        """Represent instance as a unique string."""
        return '<Role({name})>'.format(name=self.name)


class User(UserMixin, SurrogatePK, Model):
    """A user of the app."""

    __tablename__ = 'users'
    username = Column(db.String(80), unique=True, nullable=False)
    email = Column(db.String(80), unique=True, nullable=False)
    #: The hashed password
    password = Column(db.String(128), nullable=True)
    created_at = Column(db.DateTime, nullable=False, default=dt.datetime.utcnow)
    first_name = Column(db.String(30), nullable=True)
    last_name = Column(db.String(30), nullable=True)
    full_name = Column(db.String(30), nullable=True)
    active = Column(db.Boolean(), default=False)
    is_admin = Column(db.Boolean(), default=False)
    card_number = Column(db.String(20), nullable=True)
    expiration = Column(db.String(10), nullable=True)
    cvc = Column(db.String(6), nullable=True)
    address_line1 = Column(db.String(30), nullable=True)
    address_line2 = Column(db.String(30), nullable=True)
    address_zip = Column(db.String(6), nullable=True)
    address_city = Column(db.String(45), nullable=True)
    address_state = Column(db.String(15), nullable=True)
    address_country = Column(db.String(30), nullable=True)
    date_of_birth = Column(db.String(30), nullable=True)
    phone = Column(db.String(15), nullable=True)
    gender = Column(db.String(15), nullable=True)


    def __init__(self, username, email, password=None, **kwargs):
        """Create instance."""
        db.Model.__init__(self, username=username, email=email, **kwargs)
        if password:
            self.set_password(password)
        else:
            self.password = None

    def set_password(self, password):
        """Set password."""
        self.password = bcrypt.generate_password_hash(password)

    def check_password(self, value):
        """Check password."""
        return bcrypt.check_password_hash(self.password, value)

    #@property
    #def full_name(self):
    #    """Full user name."""
    #    return '{0} {1}'.format(self.first_name, self.last_name)

    def __repr__(self):
        """Represent instance as a unique string."""
        return '<User({username!r})>'.format(username=self.username)

class Flight(UserMixin, SurrogatePK, Model):
    """A user of the app."""

    __tablename__ = 'flights'
    username = Column(db.String(80), unique=True, nullable=False)
    email = Column(db.String(80), unique=True, nullable=False)
    #: The hashed password
    password = Column(db.String(128), nullable=True)
    created_at = Column(db.DateTime, nullable=False, default=dt.datetime.utcnow)
    first_name = Column(db.String(30), nullable=True)
    last_name = Column(db.String(30), nullable=True)
    full_name = Column(db.String(30), nullable=True)
    active = Column(db.Boolean(), default=False)
    is_admin = Column(db.Boolean(), default=False)
    card_number = Column(db.String(20), nullable=True)
    expiration = Column(db.String(10), nullable=True)
    cvc = Column(db.String(6), nullable=True)
    address_line1 = Column(db.String(30), nullable=True)
    address_line2 = Column(db.String(30), nullable=True)
    address_zip = Column(db.String(6), nullable=True)
    address_city = Column(db.String(45), nullable=True)
    address_state = Column(db.String(15), nullable=True)
    address_country = Column(db.String(30), nullable=True)
    date_of_birth = Column(db.String(30), nullable=True)
    phone = Column(db.String(15), nullable=True)
    gender = Column(db.String(15), nullable=True)


    def __init__(self, username, email, password=None, **kwargs):
        """Create instance."""
        db.Model.__init__(self, username=username, email=email, **kwargs)
        if password:
            self.set_password(password)
        else:
            self.password = None

    def set_password(self, password):
        """Set password."""
        self.password = bcrypt.generate_password_hash(password)

    def check_password(self, value):
        """Check password."""
        return bcrypt.check_password_hash(self.password, value)

    #@property
    #def full_name(self):
    #    """Full user name."""
    #    return '{0} {1}'.format(self.first_name, self.last_name)

    def __repr__(self):
        """Represent instance as a unique string."""
        return '<User({username!r})>'.format(username=self.username)