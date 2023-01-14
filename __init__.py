from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SECRET_KEY'] = '7dc999dc13b12c82360a4ca92411f6a9'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'


db = SQLAlchemy(app)

with app.app_context():
    db.create_all()

from fitvidapphackathon import routes 
# line 16 might need to be in line 12 - not sure but it seems to be working at the moment