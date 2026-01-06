import re

from flask_wtf import FlaskForm
from wtforms import (
    StringField, PasswordField, SubmitField, 
    DecimalField, DateField, TimeField, FileField, TextAreaField
)
from wtforms.validators import (
    DataRequired, Email, Length, EqualTo, ValidationError, NumberRange
)
from flask_wtf.file import FileAllowed
from app.models.user import User


# --- Custom Validators ---
def strong_password(form, field):
    password = field.data
    if len(password) < 8:
        raise ValidationError("Password must be at least 8 characters long.")
    if not re.search(r"[A-Z]", password):
        raise ValidationError("Password must contain at least one uppercase letter.")
    if not re.search(r"[a-z]", password):
        raise ValidationError("Password must contain at least one lowercase letter.")
    if not re.search(r"\d", password):
        raise ValidationError("Password must contain at least one digit.")
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        raise ValidationError("Password must contain at least one special character.")


# --- Registration Form ---
class RegistrationForm(FlaskForm):
    username = StringField(
        "Username",
        validators=[DataRequired(), Length(min=4, max=30)],
    )
    email = StringField(
        "Email",
        validators=[DataRequired(), Email(), Length(max=150)],
    )
    password = PasswordField(
        "Password",
        validators=[DataRequired(), strong_password],
    )
    confirm_password = PasswordField(
        "Confirm Password",
        validators=[DataRequired(), EqualTo("password", message="Passwords must match")],
    )
    submit = SubmitField("Register")

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data.lower().strip()).first()
        if user:
            raise ValidationError("Email is already registered")

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data.strip()).first()
        if user:
            raise ValidationError("Username is already taken")


# --- Login Form ---
class LoginForm(FlaskForm):
    email = StringField(
        "Email",
        validators=[DataRequired(), Email(), Length(max=150)],
    )
    password = PasswordField(
        "Password",
        validators=[DataRequired()],
    )
    submit = SubmitField("Login")


# --- Forgot Password Form ---
class ForgotPasswordForm(FlaskForm):
    email = StringField(
        "Email",
        validators=[DataRequired(), Email()],
    )
    submit = SubmitField("Send Reset Link")


# --- Reset Password Form ---
class ResetPasswordForm(FlaskForm):
    password = PasswordField(
        "New Password",
        validators=[DataRequired(), Length(min=8)],
    )
    confirm_password = PasswordField(
        "Confirm Password",
        validators=[DataRequired(), EqualTo("password")],
    )
    submit = SubmitField("Reset Password")


# --- Expense Form ---
class ExpenseForm(FlaskForm):
    date = DateField(
        "Date",
        validators=[DataRequired()],
        format="%Y-%m-%d"
    )
    time = TimeField(
        "Time",
        validators=[DataRequired()],
        format="%H:%M"
    )
    description = TextAreaField(
        "Description",
        validators=[DataRequired(), Length(max=200)],
        render_kw={"placeholder": "E.g. Grocery shopping"}
    )
    amount = DecimalField(
        "Amount (USD)",
        validators=[DataRequired(), NumberRange(min=0)],
        places=2
    )
    receipt = FileField(
        "Upload Receipt",
        validators=[FileAllowed(['jpg', 'jpeg', 'png', 'pdf'], 'Images and PDFs only!')]
    )
    submit = SubmitField("Add Expense")
