from flask_login import LoginManager
from flask_mail import Mail
from flask_wtf.csrf import CSRFProtect

# Initialize extensions
login_manager = LoginManager()
mail = Mail()
csrf = CSRFProtect()

# Configure login view
login_manager.login_view = "user_api.login"
