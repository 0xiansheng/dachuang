from flask import Blueprint,render_template
from exts import mail
from flask_mail import Message
#url_prefix:作为前缀 127.0.0.1:5000/user
bp = Blueprint("user",__name__,url_prefix="/user")

@bp.route("/login")
def login():
    return render_template("Login.html")

@bp.route("/register")
def register():
    return render_template("register.html")

@bp.route("/mail")
def my_mail():
    message = Message(
        subject="邮箱测试",
        recipients=['1252967009@qq.com'],
        body="这是一篇测试邮件"
    )
    mail.send(message)
    return "success"