from flask_wtf import FlaskForm
from wtforms import (StringField, PasswordField, SubmitField, RadioField, DateField,FileField,MultipleFileField,SelectField,IntegerField,TextAreaField,BooleanField)
from wtforms.validators import InputRequired,DataRequired,Length,EqualTo
from flask import flash

class FirstForm(FlaskForm):
    name = StringField("your name", validators=[DataRequired()])
    submit = SubmitField("save")

    def handle(self):
        if self.name.data:
            name = self.name.data
        else:
            name = None
        return name

user_list = {
    "jackyu": {"passwd": "123", "name": "jackyu", "comments": [('Wed Nov 17 10:09:09 2020',"今天心情不好")]}

}

class RegisterForm(FlaskForm):
    name = StringField('用户名:',validators=[DataRequired()])
    passwd = PasswordField("密码:", validators=[DataRequired(), Length(3,12)])
    confirm = PasswordField("确认密码:",validators=[DataRequired(), EqualTo("passwd")])
    submit = SubmitField("提交")

    def handle(self):
        print(self.validate_on_submit())
        if self.validate_on_submit():
            if self.name.data in user_list:
                flash("用户名已经存在")
                return False
            else:
                flash("Success")
                user_list[self.name.data] = {"passwd": self.passwd.data, "name": self.name.data,"comments":[]}
                print(user_list)
                return True

def validate_login(request):
    print(user_list)
    name = request.form.get("name")
    passwd = request.form.get("passwd")
    print(name, passwd)
    if name and passwd:
        if name in user_list:
            if passwd == user_list[name].get("passwd"):
                return True
    else:
        return False

def validate_user(session):
    name = session.get("name")
    passwd = session.get("passwd")
    if name and passwd:
        if name in user_list:
            if passwd == user_list[name].get("passwd"):
                return True
    else:
        return False












