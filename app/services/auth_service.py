from datetime import datetime, timedelta
from app.models import User
from app.db.database import db

# Constants for account lockout policy
MAX_LOGIN_ATTEMPTS = 4
LOCK_DURATION = timedelta(minutes=15)


def authenticate_user(email, password):
    user = User.query.filter_by(email=email).first()

    # User not found
    if not user:
        return None, "Invalid email or password"

    # Check if account is locked
    if user.is_locked():
        remaining_lock_time = int(
            (user.locked_until - datetime.utcnow()).total_seconds() / 60
        )
        return None, f"Account is locked. Try again in {remaining_lock_time} minutes"

    # Wrong password
    if not user.check_password(password):
        user.failed_login_attempts += 1

        if user.failed_login_attempts >= MAX_LOGIN_ATTEMPTS:
            user.locked_until = datetime.utcnow() + LOCK_DURATION
            user.failed_login_attempts = 0

        db.session.commit()
        return None, "Invalid email or password"

    # Successful login → reset counters
    user.failed_login_attempts = 0
    user.locked_until = None
    db.session.commit()

    return user, None
