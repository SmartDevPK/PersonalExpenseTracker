from app.models.expense import ExpenseCategory
from app.db.database import db
from app import create_app

# Create Flask app
app = create_app()

# Predefined expense categories to seed
default_categories = ["Food", "Transport", "Utilities", "Entertainment", "Healthcare"]

def seed_default_categories():
    """
    Seed the database with default expense categories if they don't already exist.
    """
    with app.app_context():
        # Create tables if they don't exist
        db.create_all()

        for name in default_categories:
            exists = ExpenseCategory.query.filter_by(name=name).first()
            if not exists:
                category = ExpenseCategory(name=name)
                db.session.add(category)

        db.session.commit()
        print("Default categories added.")

if __name__ == "__main__":
    seed_default_categories()
