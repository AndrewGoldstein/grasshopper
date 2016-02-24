"""Main application package."""


from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://hkwdxzsksohoae:mi4SH7b8_4fB4RhENknqsDj-A3@ec2-54-83-198-111.compute-1.amazonaws.com:5432/de336vejtlpkej'
db = SQLAlchemy(app)


#dbname=de336vejtlpkej host=ec2-54-83-198-111.compute-1.amazonaws.com port=5432 user=hkwdxzsksohoae password=mi4SH7b8_4fB4RhENknqsDj-A3 sslmode=require