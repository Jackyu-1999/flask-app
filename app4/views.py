from app4 import app
from flask import request, render_template, make_response, redirect
from app4.main.forms import firstForm,Form0,handle,AddProductForm



@app.route("/first/", methods=['GET', 'POST'])
def first():
    form = firstForm()
    if form.validate_on_submit():
        name = form.name.data
    else:
        name = "Jackyu"
    return render_template("first.html", form=form)

@app.route("/second/", methods=["GET","POST"])
def second():
    print(request.method)
    form = Form0()
    handle(form)
    return render_template("second.html", form=form)

@app.route("/third/", methods=["GET","POST"])
def third():
    fm = AddProductForm()
    fm.handle_pics()
    return render_template("third.html", form=fm)























