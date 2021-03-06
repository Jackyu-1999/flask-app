from flask import Flask
from flask_bootstrap import Bootstrap

app = Flask(__name__)

app.config.from_object("config")

bootstrap = Bootstrap(app)

from app4 import views

