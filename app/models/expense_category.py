from datetime import datetime
from app.db.database import db

class ExpenseCategory(db.Model):
    """
    Model representing categories for expenses.
    """
    __tablename__ = "expense_categories"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)

    # Debug representation
    def __repr__(self):
        return f"<ExpenseCategory {self.name}>"
