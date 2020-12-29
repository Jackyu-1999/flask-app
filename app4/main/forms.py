from flask_wtf import FlaskForm
from wtforms import (StringField, PasswordField, SubmitField, RadioField, DateField,FileField,MultipleFileField,SelectField,IntegerField,TextAreaField,BooleanField)

from wtforms.validators import InputRequired,DataRequired,Length,EqualTo,Email
from flask import request

class firstForm(FlaskForm):
    name = StringField("your name", validators=[DataRequired()])
    submit = SubmitField("save")

class Form0(FlaskForm):
    name = StringField("Email",validators=[DataRequired(),Email()])
    password = PasswordField("密码",validators=[InputRequired(message="密码不能为空"),Length(2,12)])
    conform = PasswordField("重复密码", validators=[InputRequired(message="密码不一致")])

    sex = RadioField("性别",choices=[("男","Male"), ("女","Female")], default="男")

    age = IntegerField("年龄")
    date = DateField("出生日期",format="%Y-%m-%d",render_kw={"placeholder": "%Y-%m-%d"})

    file = FileField("上传学历证书",validators=[InputRequired()])
    select = SelectField("选择省份", choices=["湖南","湖北"])

    textarea = TextAreaField("自我简介",render_kw={"rows":8})
    tag1 = BooleanField("宅男/女", default=False)
    tag2 = BooleanField("IT")
    tag3 = BooleanField("学生")
    tag4 = BooleanField("颜控")
    tag5 = BooleanField("铁公鸡")

    submit = SubmitField("提交")

def handle(form0):
    if form0.validate_on_submit():
        email = form0.name.data
        password = form0.password.data
        sex = form0.sex.data
        age = form0.age.data
        date = form0.date.data
        print(email, password,sex,age,date)
        file = form0.file.data
        file.save('1.png')
        print(file.filename)
        select = form0.select.data
        print(select)
        textarea = form0.textarea.data
        print(textarea)
        tag1 = form0.tag1.data
        print(tag1, form0.tag2.data, form0.tag3.data, form0.tag4.data,form0.tag5.data)


class AddProductForm(FlaskForm):
    product_pictures = MultipleFileField('Pictures')
    submit = SubmitField('提交')

    def handle_pics(self):
        if self.validate_on_submit():
            print(request.form)
            print(request.files)
            pics_data = request.files.getlist("product_pictures")
            for pics_data in pics_data:
                pics_data.save(pics_data.filename)

