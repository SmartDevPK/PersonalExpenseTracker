import pymysql
from dotenv import load_dotenv
from flask import Flask, render_template

from app.extensions import mail, csrf, login_manager
from app.db.database import db
from app.core.security import init_security
from app.config import Config
from app.api import blueprints
from app.api.user_routes import user_api

# Load environment variables early
load_dotenv()


def create_app():
    # Use PyMySQL as MySQLdb
    pymysql.install_as_MySQLdb()

    app = Flask(__name__)

    # Load configuration (SECRET_KEY, DB, MAIL, etc.)
    app.config.from_object(Config)

    # Initialize extensions
    mail.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    csrf.init_app(app)
    init_security(app)

    # Register blueprints
    for bp in blueprints:
        app.register_blueprint(bp)

    if user_api not in blueprints:
        app.register_blueprint(user_api)

    # Set Content Security Policy header
    @app.after_request
    def set_csp(response):
        response.headers["Content-Security-Policy"] = "script-src 'self' 'unsafe-eval'"
        return response

    # Home route
    @app.route("/")
    def home():
        return render_template("index.html")

    # Ensure models & user_loader are registered
    with app.app_context():
        from app.auth.user_loader import load_user  # noqa
        db.create_all()

    return app
