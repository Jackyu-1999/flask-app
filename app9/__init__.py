from flask import Flask 
from flask_mail import Mail


app = Flask(__name__)

app.config.update(
	MAIL_SERVER = 'smtp.126.com',
	MAIL_PORT = 25,
	MAIL_USE_TLS = True,
	MAIL_USE_SSL = False,
	MAIL_USERNAME = 'Jackyu1999@126.com',
	MAIL_PASSWORD = 'IAAFDJAKSZSWYHNY',
	MAIL_DEFAULT_SENDER = ('cw', 'Jackyu1999@126.com'),
	MAIL_DEBUG = True

	)
mail = Mail(app)
from app9 import views