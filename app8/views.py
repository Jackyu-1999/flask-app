from app8 import app, db
from app8.main.models import User, Comments
from app8.main.forms import RegisterForm
from flask import render_template, request, redirect, url_for, session, flash
from datetime import datetime





@app.route("/register/", methods=["GET", "POST"])
def index():
    db.create_all()
    register_form = RegisterForm()
    if register_form.handle():
        return redirect(url_for("login"))
    else:
        return render_template("register.html", form=register_form)


@app.route("/login/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        name = request.form.get("name")
        passwd = request.form.get("passwd")
        if name and passwd:
            user_q = User.query.filter_by(name=name).filter_by(passwd=passwd).first()
            if user_q:
                session["name"] = name
                session["passwd"] = passwd
                session["id"] = user_q.id
                return redirect(url_for("user"))
            else:
                flash("用户名或者密码不正确")
                return redirect(url_for("user"))

        else:
            flash("请输入有效的账号密码")
    return render_template("login.html")

@app.route('/user/', methods=["GET", "POST"])
def user():
    id = session.get("id")
    name = session.get("name")
    passwd = session.get('passwd')
    if id and name and passwd:
        user_p=User.query.filter_by(id=id).filter_by(name=name).filter_by(passwd=passwd).first()
        if user_p is None:
            return redirect(url_for("login"))

        else:
            if request.method == "GET":

                # comments_ct = Comments.query.filter_by(user_id=id)
                comments_ct = user_p.comments
                print("反向查找", comments_ct[0].user)
                return render_template("user.html", name=name,comments_ct=comments_ct)
                
            if request.method == "POST":
                textarea = request.form.get("textarea")
                if textarea:
                    says = textarea
                    user_id = id
                    datetime_now = datetime.now()
                    ct = Comments(says=says, datetime=datetime_now, user_id=user_id)
                    db.session.add(ct)
                    db.session.commit()
                else:
                    pass
                return redirect(url_for("user"))
            else:
                return redirect(url_for("login"))