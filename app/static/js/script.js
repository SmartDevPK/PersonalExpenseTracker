const expensesTableBody = document.getElementById('expensesTableBody');
const expenseModal = document.getElementById('expenseModal');
const openAddModalBtn = document.getElementById('openAddModal');
const closeModalBtn = document.getElementById('closeModal');
const cancelBtn = document.getElementById('cancelBtn');
const expenseForm = document.getElementById('expenseForm');
const modalTitle = document.getElementById('modalTitle');
const submitBtn = document.getElementById('submitBtn');

let expenses = [];
let editingIndex = null;

// Open Add Expense Modal
openAddModalBtn.addEventListener('click', () => {
  editingIndex = null;
  modalTitle.textContent = 'Add Expense';
  submitBtn.textContent = 'Add';
  expenseForm.reset();
  expenseModal.classList.add('active');
});

// Close Modal
function closeModal() {
  expenseModal.classList.remove('active');
}

closeModalBtn.addEventListener('click', closeModal);
cancelBtn.addEventListener('click', closeModal);

// Render expenses table
function renderExpenses() {
  expensesTableBody.innerHTML = '';

  expenses.forEach((expense, index) => {
    const tr = document.createElement('tr');

    tr.innerHTML = `
      <td>${expense.title}</td>
      <td>$${expense.amount.toFixed(2)}</td>
      <td>${getCategoryName(expense.category_id)}</td>
      <td>${expense.date}</td>
      <td>${expense.description}</td>
      <td>
        <button class="btn-edit" data-index="${index}">Edit</button>
        <button class="btn-delete" data-index="${index}">Delete</button>
      </td>
    `;

    expensesTableBody.appendChild(tr);
  });

  attachRowListeners();
}

// Attach listeners to edit/delete buttons
function attachRowListeners() {
  document.querySelectorAll('.btn-edit').forEach(btn => {
    btn.addEventListener('click', e => {
      const index = e.target.dataset.index;
      editExpense(index);
    });
  });

  document.querySelectorAll('.btn-delete').forEach(btn => {
    btn.addEventListener('click', e => {
      const index = e.target.dataset.index;
      deleteExpense(index);
    });
  });
}

// Edit expense
function editExpense(index) {
  editingIndex = index;
  const expense = expenses[index];

  modalTitle.textContent = 'Edit Expense';
  submitBtn.textContent = 'Update';

  expenseForm.title.value = expense.title;
  expenseForm.amount.value = expense.amount;
  expenseForm.category_id.value = expense.category_id;
  expenseForm.date.value = expense.date;
  expenseForm.description.value = expense.description;

  expenseModal.classList.add('active');
}

// Delete expense (client-side only for now)
function deleteExpense(index) {
  if (confirm('Are you sure you want to delete this expense?')) {
    expenses.splice(index, 1);
    renderExpenses();
  }
}

// Helper: Map category IDs to names
function getCategoryName(id) {
  const categories = {
    1: 'Food',
    2: 'Transport',
    3: 'Utilities',
    4: 'Entertainment',
    5: 'Healthcare'
  };
  return categories[id] || 'Unknown';
}

// Load expenses from backend API
async function loadExpensesFromServer() {
  try {
    const response = await fetch('/expenses', {
      method: 'GET',
      credentials: 'include'
    });
    if (!response.ok) {
      throw new Error('Failed to fetch expenses');
    }
    const data = await response.json();

    expenses = data.map(expense => ({
      id: expense.id,
      title: expense.title,
      amount: parseFloat(expense.amount),
      category_id: expense.category_id,
      date: expense.expense_date || '',
      description: expense.description || ''
    }));

    renderExpenses();
  } catch (err) {
    alert(`Error loading expenses: ${err.message}`);
  }
}

// Handle form submit (Add or Update)
expenseForm.addEventListener('submit', async (e) => {
  e.preventDefault();

  const expenseData = {
    title: expenseForm.title.value.trim(),
    amount: parseFloat(expenseForm.amount.value),
    category_id: expenseForm.category_id.value,
    date: expenseForm.date.value,
    description: expenseForm.description.value.trim(),
  };

  try {
    const response = await fetch('/expenses', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      credentials: 'include',
      body: JSON.stringify(expenseData),
    });

    if (!response.ok) {
      const error = await response.json();
      alert(`Error: ${error.error || 'Failed to add expense'}`);
      return;
    }

    const newExpense = await response.json();

    if (editingIndex === null) {
      expenses.push({
        id: newExpense.id,
        title: newExpense.title,
        amount: parseFloat(newExpense.amount),
        category_id: newExpense.category_id,
        date: newExpense.expense_date || '',
        description: newExpense.description || ''
      });
    } else {
      expenses[editingIndex] = {
        id: newExpense.id,
        title: newExpense.title,
        amount: parseFloat(newExpense.amount),
        category_id: newExpense.category_id,
        date: newExpense.expense_date || '',
        description: newExpense.description || ''
      };
    }

    renderExpenses();
    expenseForm.reset();
    closeModal();
    editingIndex = null;

  } catch (err) {
    alert(`Network error: ${err.message}`);
  }
});

// Initial load of expenses from server
loadExpensesFromServer();
