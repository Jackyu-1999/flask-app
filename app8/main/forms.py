from flask_wtf import FlaskForm
from app8 import db
from wtforms import (StringField, PasswordField, SubmitField, RadioField, DateField,FileField,MultipleFileField,SelectField,IntegerField,TextAreaField,BooleanField)
from wtforms.validators import InputRequired,DataRequired,Length,EqualTo
from flask import flash
from app8.main.models import User

class RegisterForm(FlaskForm):
	name = StringField("用户名:", validators=[DataRequired()])
	passwd = PasswordField("密码:", validators=[DataRequired(),Length(3,12)])
	confirm = PasswordField("确认密码:", validators=[DataRequired(),EqualTo("passwd")])
	submit = SubmitField("提交")

	def handle(self):
		if self.validate_on_submit():
			user = User.query.filter_by(name=self.name.data).first()
			if user is not None:
				flash("用户名已经存在")
				return False

			else:
				user = User(name=self.name.data, passwd=self.passwd.data)
				db.session.add(user)
				db.session.commit()
				flash('成功，您的用户名是 %s' % user.name)
				return True
		else:
			return False