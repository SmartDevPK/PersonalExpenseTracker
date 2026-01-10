from flask import Blueprint, request, jsonify
from flask_login import login_required, current_user
from datetime import datetime
from app.models.expense import Expense

from app.extensions import csrf
from app.services.expense_service import add_expense

expenses_bp = Blueprint('expenses', __name__)

@csrf.exempt
@expenses_bp.route('/expenses', methods=['GET', 'POST'])
@login_required
def expenses():
    if request.method == 'GET':
        # Handle fetching expenses
        user_id = current_user.id
        expenses = Expense.query.filter_by(user_id=user_id).order_by(Expense.expense_date.desc()).all()

        expenses_list = [{
            "id": e.id,
            "title": e.title,
            "amount": float(e.amount),
            "description": e.description,
            "category_id": e.category_id,
            "expense_date": e.expense_date.isoformat() if e.expense_date else None,
            "created_at": e.created_at.isoformat(),
            "updated_at": e.updated_at.isoformat(),
        } for e in expenses]

        return jsonify(expenses_list)

    elif request.method == 'POST':
        data = request.get_json(silent=True)
        if not data:
            return jsonify({"error": "Invalid or missing JSON"}), 400

        # Validate required fields
        title = data.get("title")
        category_id = data.get("category_id")
        amount = data.get("amount")

        if not title or not category_id:
            return jsonify({"error": "Title and category are required"}), 400

        if amount is None:
            return jsonify({"error": "Amount is required"}), 400

        try:
            amount = float(amount)
            if amount <= 0:
                raise ValueError
        except (TypeError, ValueError):
            return jsonify({"error": "Amount must be a positive number"}), 400

        description = data.get("description")
        expense_date_str = data.get("date")

        if expense_date_str:
            try:
                expense_date = datetime.fromisoformat(expense_date_str).date()
            except ValueError:
                return jsonify({"error": "Invalid date format"}), 400
        else:
            expense_date = None

        user_id = current_user.id

        expense = add_expense(
            user_id=user_id,
            title=title,
            amount=amount,
            description=description,
            category_id=category_id,
            expense_date=expense_date
        )

        return jsonify({
            "id": expense.id,
            "title": expense.title,
            "amount": float(expense.amount),
            "description": expense.description,
            "category_id": expense.category_id,
            "expense_date": expense.expense_date.isoformat() if expense.expense_date else None,
            "created_at": expense.created_at.isoformat(),
            "updated_at": expense.updated_at.isoformat(),
        }), 201
