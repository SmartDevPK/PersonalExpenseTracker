from datetime import datetime
from app.db.database import db
from app.models.expense_category import ExpenseCategory

class Expense(db.Model):
    """
    Model representing an expense entry.
    """
    __tablename__ = "expenses"

    # Primary key
    id = db.Column(db.Integer, primary_key=True)
    
    # Foreign key to the user who owns the expense
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    
    # Expense details
    title = db.Column(db.String(150), nullable=False)
    amount = db.Column(db.Numeric(10, 2), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey("expense_categories.id"), nullable=False)
    description = db.Column(db.Text, nullable=False)
    expense_date = db.Column(db.Date, nullable=False)
    
    # Timestamp fields
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

    # Relationships
    user = db.relationship("User", backref="expenses")
    category = db.relationship("ExpenseCategory", backref="expenses")

    def __repr__(self):
        return f"<Expense {self.title} - {self.amount}>"
