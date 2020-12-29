from app5 import app
from flask import request, render_template, make_response, redirect,session,url_for, flash
from app5.main.forms import FirstForm, RegisterForm,validate_login,validate_user,user_list
import time


@app.route("/first/", methods=['GET', 'POST'])
def first():
    form = FirstForm()
    if form.validate_on_submit():
        session['name'] = form.handle()
        return redirect(url_for("first"))
    return render_template("first.html", form=form, name=session.get("name"))




@app.route("/second/", methods=["GET","POST"])
def second():
    flash("your have a message from url now")
    flash("你获得了一条来自服务器的消息")
    return render_template("second.html")


# 闪消息
@app.route("/third/", methods=["GET","POST"])
def third():
    form = FirstForm()
    if form.validate_on_submit():
        name = form.handle()
        old_name = session.get("name")
        print(name, old_name)
        if name and old_name:
            if name != old_name:
                flash(f"你看起来好像改了名字,form(old_name) to {name}!")
        session["name"] = form.handle()
        return redirect(url_for("third"))

    return render_template("third.html", form=form, name=session.get("name"))


@app.route("/login/", methods=["GET","POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    if request.method == "POST":
        if validate_login(request):
            session["name"] = request.form.get("name")
            session["passwd"] = request.form.get("passwd")
            return redirect("/user/")
        else:
            flash("用户名或密码错误")
            return redirect("/login/")




@app.route("/register/", methods=["GET","POST"])
def register():
    register_form = RegisterForm()
    if register_form.handle():
        return redirect("/login/")

    else:
        return render_template("register.html", form=register_form)

@app.route("/user/", methods=["GET","POST"])
def user():
    if validate_user(session):
        if request.method == "POST":
            comment = request.form.get("textarea")
            time_s = time.asctime(time.localtime(time.time()))
            print(time_s, comment)
            user_list[session['name']]["comments"].append((time_s, comment))
            return redirect("/user/")
        comments = user_list[session['name']].get("comments")
        return render_template("user.html", name=session["name"], comments=reversed(comments))
    else:
        return redirect("/login/")













