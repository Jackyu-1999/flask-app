
user_list = {
    "123@qq.com": ["jackyu", "123", "seven.gif"],
    "1234@qq.com": ["joker", "123", "Harry Port.jpg"]
}


def validate_login(request):
    email = request.cookies.get("user", None)
    passwd = request.cookies.get("passwd", None)
    if email and passwd:
        if email in user_list:
            if user_list[email] [1] == passwd:
                return True
    else:
        return False