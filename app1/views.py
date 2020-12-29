from app1 import app
from flask import request, render_template, make_response, redirect
import time


@app.route("/hello/")

def hello():
    response = make_response("WELCOME TO HOME")
    response.delete_cookie = ("time")
    return response


@app.route("/")
@app.route("/request/")
def show_request():
    content = render_template("show_request.html", request=request)
    response = make_response()
    response.set_data(content)
    response.set_cookie("time", str(time.time()))
    if request.cookies.get("time", None):
        if time.time() - float(request.cookies["time"]) > 2:
            return redirect("/hello/")


    return response