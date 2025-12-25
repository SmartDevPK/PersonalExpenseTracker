from flask import Blueprint, render_template

auth = Blueprint('auth', __name__)

# Define a route for the login page
@auth.route("/login")
def login():
    return render_template("login.html")

# Define a route for the registration page
@auth.route("/register")
def register():
    return render_template("register.html")
