from flask import Blueprint, render_template

user_api = Blueprint('user_api', __name__)

@user_api.route("/login")
def login():
    return render_template("login.html")

@user_api.route("/register")
def register():
    return render_template("register.html")
