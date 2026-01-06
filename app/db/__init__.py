from flask_sqlalchemy import SQLAlchemy


# Initialize SQLAlchemy
db = SQLAlchemy()

# Additional database-related setup can be added here
__all__ = ['db']