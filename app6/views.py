from app6 import app, db
from app6.main.models import User
from flask import render_template, request, redirect, url_for

@app.route("/", methods=["GET", "POST"])
def index():
    db.create_all()

    users = User.query.all()
    if request.method == "POST":
        id = request.form.get("id")
        name = request.form.get("name")
        passwd = request.form.get("passwd")

        if id and name and passwd:
            user_update = User.query.filter_by(id=id).first()
            user_update.name = name
            user_update.passwd = passwd
            db.session.add(user_update)
            db.session.commit()
            return redirect(url_for("index"))

        new_name = request.form.get("new_name")
        new_passwd = request.form.get("new_passwd")
        
        if new_name and new_passwd:
            new_user = User(name=new_name, passwd=new_passwd)
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for("index"))
            
    if request.args.get("delete_id"):
        id = request.args.get("delete_id")
        user_delete = User.query.filter_by(id=id).first()
        if user_delete:
            db.session.delete(user_delete)
            db.session.commit()
        return redirect(url_for("index"))

    return render_template("admin.html", users=users)

