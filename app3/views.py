from app3 import app
from flask import request, render_template, make_response, redirect
from app3.main.models import mydict,mylist,myobj,comments
from app3.main.validates import validate_login, user_list
import hashlib


@app.route("/first/")
def first():
    name = "Jackyu"
    image = '../static/img/seven.gif'
    return render_template("first.html", name=name, image=image)

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
        response = redirect("/user/")
        response.set_cookie("user", request.form["user"])
        response.set_cookie("passwd", request.form["password"])
        return response



# 加密
# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'GET': # 浏览器访问
#         return render_template("login.html")
#     if request.method == 'POST': # form提交处理逻辑
#         username = request.form['username']
#         pwd_temp = hashlib.sha1(request.form['password'])# sha1哈希加密
#         password = pwd_temp.hexdigest()# sha1哈希加密
#         checkcode = request.form['checkcode']
#         if isNameExist(username): # 用户名已经存在
#             return 'nameisexisted'
#         elif not isCheckCode(checkcode): # 验证码不正确
#             return 'checkcodeerror'
#         else:
#             setNewAdmin(username, password,checkcode)
#             return 'success'


@app.route("/user/", methods=["GET", "POST"])
def user():
    if validate_login(request):
        name = user_list[request.cookies['user']][0]
        image = user_list[request.cookies['user']][2]
        response = make_response(render_template('user.html', name=name, image=image))
    else:
        return redirect('/login/')
    return response

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404
@app.route("/error/")
def raise_500():
    raise ZeroDivisionError

@app.errorhandler(500)
def internal_server_error(e):
    return render_template("500.html"), 500






























