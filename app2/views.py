from app2 import app
from flask import request, render_template, make_response, redirect
from app2.main.models import mydict,mylist,myobj,comments


@app.route("/first/")
def first():
    name = "Jackyu"
    age = 20
    return render_template("first.html", name=name, age=age)

@app.route("/second/")
def second():
    return render_template("second.html", mydict=mydict,mylist=mylist,myobj=myobj)

@app.route("/third/")
def third():
    return render_template("third.html", comments=comments)

@app.route("/four/")
def four():
    return render_template("four.html", name="joker",comments=comments)

@app.route("/login/", methods=["GET", "POST"])

def login():
    if request.method == "GET":
        return render_template("login.html")

    if request.method == "POST":
        user = request.form['user']
        password = request.form["password"]
        print(user)
        print(password)
        response = make_response("<h1>welcome {} </h1>".format(request.form['user']))
        if request.form.get("check",None):
            response.set_cookie("user", user)
            response.set_cookie("password", password)
        return response
































