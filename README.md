## About ExpenseTracker

ExpenseTracker is a user-friendly application designed to help individuals, business owners, cooperatives, government and private organizations, as well as students efficiently track their daily, weekly, and monthly expenses. The app provides a simple interface to add, view, and manage expenses, making budgeting and financial management easier.

Built using Python, FastAPI, and MySQL, ExpenseTracker features secure user authentication including registration, login, password reset, and welcome notifications. This tool empowers users to maintain better control over their finances and make informed spending decisions.

Developer: DevPk

## Project Structure
ExpenseTracker/
├── app/
│   ├── api/
│   │   ├── __init__.py
│   │   ├── user_routes.py
│   │   └── ... 
│   ├── models/
│   │   ├── __init__.py
│   │   └── user.py
│   ├── services/
│   │   ├── email_service.py
│   │   ├── forms.py
│   │   └── auth_service.py
│   ├── extensions.py
│   ├── db/
│   │   ├── database.py
│   │   └── migrations/
│   ├── templates/
│   │   ├── dashboard.html
│   │   ├── login.html
│   │   ├── register.html
│   │   └── ...
│   ├── static/
│   │   ├── css/
│   │   ├── js/
│   │   └── images/
│   ├── config.py
│   └── main.py  # Or app.py, your Flask/FastAPI app entry point
├── tests/
│   └── test_auth.py
├── .env
├── .gitignore
├── requirements.txt
└── README.md

## Environment Variables (.env)

This project uses a `.env` file to manage environment-specific configurations such as database credentials, secret keys, and email settings.

### Required variables

Create a `.env` file in the root directory of the project with the following variables:

```env
MYSQL_USERNAME=root
MYSQL_PASSWORD=
MYSQL_HOST=localhost
MYSQL_PORT=3306
MYSQL_DB=PersonalExpenseTracker
```
