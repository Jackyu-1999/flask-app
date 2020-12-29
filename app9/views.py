from app9 import app, mail
from flask_mail import Message



@app.route('/')
def index():
    msg = Message(subject='this is a test for e-mail', recipients=['heartlessdevil99@qq.com'])
    msg.body = 'this e-mail is for myself'
    mail.send(msg)
    return 'ok'