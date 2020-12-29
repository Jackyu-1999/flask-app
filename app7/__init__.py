from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
import pymysql
pymysql.install_as_MySQLdb()

app = Flask(__name__)
app.config.from_object("config")

bootstrap = Bootstrap(app)
db = SQLAlchemy(app)


from app7 import views

