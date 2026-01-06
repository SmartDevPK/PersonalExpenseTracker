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

## gitignore

The .gitignore file tells Git which files or directories to ignore and not track in the repository. This is essential for excluding files that are environment-specific, contain sensitive data, or are generated automatically (like logs, caches, or compiled files).

.env
__pycache__/
*.pyc
instance/
*.log

## Application Initialization

The `app/__init__.py` file contains the Flask application factory function `create_app()`. This function:

- Loads environment variables early using `python-dotenv`.
- Configures Flask to use PyMySQL as the MySQLdb driver.
- Creates a Flask app instance and loads configuration settings from the `Config` class.
- Initializes core Flask extensions including:
  - Flask-Mail for email support
  - SQLAlchemy for database ORM
  - Flask-Login for user session management
  - CSRF protection with Flask-WTF
  - Custom security setup via `init_security`
- Registers all API blueprints for modular routing.

## Notes
- I refactored `app/api/__init__.py` to improve how API blueprints are initialized.
- I made this change to keep route registration clean and to avoid potential circular import issues.

## Notes
- I expanded `app/api/user_routes.py` to handle full user authentication flows.
- This includes registration, login, logout, password reset, and form handling.
- I structured the routes to integrate CSRF protection, database access, and reusable service layers.

## Notes

- I implemented full user authentication routes in `app/api/user_routes.py`.
- This includes registration, login, logout, and password recovery workflows.
- I integrated Flask-Login, CSRF protection, and form validation while keeping business logic in service layers.
- This structure improves maintainability and keeps user-related concerns isolated within the API layer.

## Notes
- Added `app/config.py` to centralize configuration using environment variables.
- The `Config` class handles database connection settings, secret key management, and mail server configuration.
- This setup improves security by loading sensitive information from `.env` and supports easy configuration changes across environments.


## Notes

- Added `app/core/security.py` to configure Cross-Origin Resource Sharing (CORS) for API endpoints.
- The `init_security` function reads allowed origins from environment variables, improving security and flexibility.
- This setup ensures that only specified frontends can access the API while supporting credentials like cookies.




