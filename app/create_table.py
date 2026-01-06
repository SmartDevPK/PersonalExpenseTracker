from dotenv import load_dotenv
from flask_mail import Mail

from app import create_app
from app.db.database import db

# Load environment variables FIRST
load_dotenv()

# Create Flask app
app = create_app()

# Initialize Flask-Mail
mail = Mail(app)

# Database operations must run inside app context
with app.app_context():
    # db.drop_all()
    # print("Tables dropped successfully")
    db.create_all()
    print("Tables created successfully")