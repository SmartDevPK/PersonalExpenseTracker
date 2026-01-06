from datetime import datetime, timedelta
import secrets

from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from app.db.database import db


class User(db.Model, UserMixin):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)

    username = db.Column(db.String(150), unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    reset_token = db.Column(db.String(100), nullable=True, unique=True)
    reset_token_expiry = db.Column(db.DateTime, nullable=True)
    password_hash = db.Column(db.String(255), nullable=False)

    failed_login_attempts = db.Column(db.Integer, default=0)
    locked_until = db.Column(db.DateTime, nullable=True)

    # Password reset token management
    def generate_reset_token(self):
        self.reset_token = secrets.token_urlsafe(32)
        self.reset_token_expiry = datetime.utcnow() + timedelta(hours=1)
        db.session.commit()
        return self.reset_token

    def clear_reset_token(self):
        self.reset_token = None
        self.reset_token_expiry = None
        db.session.commit()

    # Account lock helper
    def is_locked(self):
        return self.locked_until is not None and self.locked_until > datetime.utcnow()

    # Password property and verification
    @property
    def password(self):
        raise AttributeError("Password is not a readable attribute")

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    # Debug representation
    def __repr__(self):
        return f"<User {self.email}>"
