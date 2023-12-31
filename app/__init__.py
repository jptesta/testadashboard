from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


from app.transportadoras.transportadoras import transportadora_blueprint
from app.representadas.representadas import representadas_blueprint

app = Flask(__name__)


app.config['SECRET_KEY'] = '1234567890OIUYTREWQASDFGHJK'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///testa.db'


db = SQLAlchemy(app)
migrate = Migrate(app, db)



app.register_blueprint(transportadora_blueprint)
app.register_blueprint(representadas_blueprint)

'''
ou
app.secret_key = 'secret@@@##$)(*&¨%$#@' 
'''
from app.model import tables
from app.controllers import default
