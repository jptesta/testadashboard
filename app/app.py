from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)

app.config['SECRET_KEY'] = '1234567890OIUYTREWQASDFGHJK'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///testa.db'

db = SQLAlchemy(app)
migrate = Migrate(app, db)


'''
ou
app.secret_key = 'secret@@@##$)(*&¨%$#@' 
'''

from app.controllers import default
from app.model import tables


