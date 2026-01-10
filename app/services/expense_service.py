from datetime import datetime
from app.db.database import db
from app.models.expense import Expense

def add_expense(user_id, title, amount, description, category_id, expense_date=None):
    """
    Create and save a new Expense record in the database.

    Parameters:
        user_id (int): ID of the user who owns the expense
        title (str): Title or name of the expense
        amount (float): Amount spent (must be positive)
        description (str): Optional description of the expense
        category_id (int): ID of the expense category
        expense_date (date or None): Date of the expense; defaults to today if None

    Returns:
        Expense: The saved Expense instance with generated ID and timestamps
    """
    if expense_date is None:
        expense_date = datetime.utcnow().date()

    expense = Expense(
        user_id=user_id,
        title=title,
        amount=amount,
        description=description,
        category_id=category_id,
        expense_date=expense_date,
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )

    db.session.add(expense)
    db.session.commit()

    return expense
