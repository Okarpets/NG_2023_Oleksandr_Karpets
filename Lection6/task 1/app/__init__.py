from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import sys

app = Flask(__name__)
app.config.from_object(Config)
app.config['SECRET_KEY'] = 'sdafagagagdw54356%$ghfhgerrr' #Secret key to use Flash
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes, models