from datetime import datetime
from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_user, login_required, current_user, logout_user
from app.models import User
from app.services.email_service import send_password_reset_email
from app.services.forms import (
    RegistrationForm, LoginForm, ForgotPasswordForm, ResetPasswordForm, ExpenseForm
)
from app.services.RegistrationForm import register_user
from app.services.auth_service import authenticate_user
from app.db.database import db
from app.extensions import csrf

user_api = Blueprint("user_api", __name__)

# --- Registration Route ---
@user_api.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        success, error = register_user(form)
        if success:
            flash("Registration successful. Welcome email sent!", "success")
            return redirect(url_for("user_api.login"))
        flash(error or "Registration failed", "danger")
    return render_template("register.html", form=form)

# --- Login Route ---
@user_api.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user, error = authenticate_user(form.email.data, form.password.data)
        if not user:
            flash(error, "danger")
            return redirect(url_for("user_api.login"))
        login_user(user)
        flash("Logged in successfully.", "success")
        return redirect(url_for("user_api.dashboard"))
    return render_template("login.html", form=form)

# --- Dashboard Route ---
@user_api.route("/dashboard", methods=["GET", "POST"])
@login_required
def dashboard():
    form = ExpenseForm()  # uncomment and create the form
    return render_template("dashboard.html", form=form)  # pass form here


# --- Forgot Password Route ---
@csrf.exempt
@user_api.route("/forgot-password", methods=["GET", "POST"])
def forgot_password():
    form = ForgotPasswordForm()
    if form.validate_on_submit():
        email = form.email.data.lower().strip()
        user = User.query.filter_by(email=email).first()
        if user:
            token = user.generate_reset_token()
            send_password_reset_email(user.email, token)
        # Always show this message regardless of whether user exists, for security
        flash("If the email exists, a reset link has been sent.", "info")
        return redirect(url_for("user_api.login"))
    return render_template("forgot_password.html", form=form)

# --- Reset Password Route ---
@csrf.exempt
@user_api.route("/reset-password/<token>", methods=["GET", "POST"])
def reset_password(token):
    user = User.query.filter_by(reset_token=token).first()
    if not user or user.reset_token_expiry < datetime.utcnow():
        flash("Invalid or expired reset token.", "danger")
        return redirect(url_for("user_api.forgot_password"))

    form = ResetPasswordForm()
    if form.validate_on_submit():
        user.password = form.password.data  # hashes password
        user.clear_reset_token()
        db.session.commit()
        flash("Your password has been reset successfully. Please log in.", "success")
        return redirect(url_for("user_api.login"))

    return render_template("reset_password.html", form=form, token=token)
# --- Logout Route ---
@user_api.route("/logout")
@login_required
def logout():
    logout_user()
    flash("You have been logged out successfully.", "success")
    return redirect(url_for("user_api.login"))


 



