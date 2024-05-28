from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SECRET_KEY'] = "AWSEDRFTGYHUJIKOLPMNV=FHGJGNNMVNVNBJTHTUYOYOHK"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///analyseDB.db'

db = SQLAlchemy(app)

from application import routes

