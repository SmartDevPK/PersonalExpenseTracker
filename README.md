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


## Notes

- Added `app/db/__init__.py` to initialize the SQLAlchemy database instance.
- Centralizes the database setup, allowing easy import of `db` across the app.
- Prepared the codebase for scalable database management and ORM usage.


## Notes

- Added `app/db/database.py` to initialize the SQLAlchemy instance separately.
- This modular approach supports better organization and easier imports across the ap

## Notes

- Refactored `app/main.py` to use the Flask application factory pattern by importing and calling `create_app()`.
- This improves app modularity and supports easier testing and configuration.
- Removed direct blueprint registration and route definition in favor of centralized setup in the factory.

## Notes

- Added `app/models/__init__.py` to initialize the models package and import the `User` model.
- This setup enables clean and centralized model imports throughout the app.
- Prepared for scalable addition of other models as the project grows.

## Notes

- Added `app/models/user.py` defining the `User` model for authentication.
- Includes fields for username, email, password hash, and login security (failed attempts, lockout).
- Implements secure password reset token generation and expiry handling.
- Uses Flask-Login's `UserMixin` for session management integration.

## Notes

- Added `app/schemas/__init__.py` to initialize the schemas package.
- Imported `UserSchema` for centralized schema management.
- This structure supports scalable addition of data serialization schemas.

## Notes
- Added `app/schemas/user_schema.py` defining `UserSchema` using Marshmallow.
- Schema handles serialization and validation of user data.

## Notes
- Added `app/services/__init__.py` to initialize the services package.
- Exported key service functions like `send_welcome_email` and `register_user` for centralized imports.
- This setup supports modular and maintainable business logic separation.
 Includes fields for id (read-only), username, email, and password (write-only).

## Notes

- Updated `login.html` and `register.html` templates to improve user authentication UI/UX.
- Modified `requirements.txt` to reflect new or updated Python dependencies necessary for the project.

## Notes

- Added/updated authentication-related functionality in `app/auth/`.
- Updated `README.md` to document recent authentication module changes and improvements.

## Notes

- Added `app/create_table.py` to handle database table creation and schema setup.
- This script facilitates initial database setup and can be extended for migrations.

## Notes

- Added `app/extensions.py` to centralize initialization and configuration of Flask extensions.
- This approach improves modularity and keeps extension setup organized across the application.

## Notes

- Added `app/services/RegistrationForm.py` to handle user registration logic.
- Encapsulates validation, user creation, and related business rules in a dedicated service layer.
- Improves separation of concerns and keeps registration workflow modular and testable.

## Notes

- Added `app/services/auth_service.py` to manage user authentication processes.
- Encapsulates login verification, session handling, and security checks.
- Keeps authentication logic modular and reusable across the application.

## Notes

- Added `app/services/email_service.py` to encapsulate email-related functionality.
- Handles sending password reset, welcome, and notification emails.
- Centralizes email logic for easier management and future enhancements.



## Notes

- Added `app/services/forms.py` to define form classes for user input validation.
- Supports registration, login, password reset, and other form handling.
- Enhances data integrity and user experience with built-in validations.

## Notes

- Added `app/services/welcomeEmail.py` to manage sending welcome emails to new users.
- Centralizes welcome email logic for easier maintenance and customization.

## Notes

- Added new HTML templates:  
  - `dashboard.html` for user dashboard UI  
  - `forgot_password.html` for initiating password reset  
  - `reset_password.html` for completing password reset  
- These templates improve user experience for account management flows.

### Added Expenses Blueprint

- Registered the `expenses_bp` blueprint in `app/__init__.py` to handle expense-related API routes.
- This allows the application to manage expenses through the new endpoints provided by the `expenses` module.

### Dashboard Improvements

- Enhanced the dashboard UI with improved styling for better user experience.
- Updated HTML and CSS to create a cleaner, more modern layout.

## API - Expenses Endpoint

The `app/api/expenses.py` module defines the backend API routes for managing expenses. It includes:

- **GET /expenses**: Retrieves the list of expenses for the authenticated user.
- **POST /expenses**: Adds a new expense for the authenticated user.

These endpoints require user authentication and handle data validation, ensuring that only valid expense data is saved.

The API communicates using JSON format, making it easy to integrate with frontend applications or other services.

---

### Example Usage

- Fetch all expenses:

```bash
GET /expenses

## Expense Model

The `app/models/expense.py` file defines the `Expense` model, which represents an expense record in the database.

### Key Features:
- Stores expense details such as title, amount, description, category, and date.
- Tracks timestamps for creation and updates.
- Linked to a user to associate expenses with the owner.
- Supports categorization through a foreign key to expense categories.

This model is used by the API and service layers to manage expense data persistently.

---

### Example fields:
- `id`: Unique identifier
- `user_id`: Reference to the owner user
- `title`: Name or description of the expense
- `amount`: Expense amount (decimal)
- `description`: Optional details
- `category_id`: Expense category reference
- `expense_date`: Date of the expense
- `created_at`, `updated_at`: Timestamp fields


## ExpenseCategory Model

The `app/models/expense_category.py` file defines the `ExpenseCategory` model, representing categories for expenses.

### Key Features:
- Stores category names for organizing expenses.
- Ensures unique category names to avoid duplicates.
- Used to link expenses to specific categories for better tracking and reporting.

---

### Example fields:
- `id`: Unique identifier for the category  
- `name`: Name of the expense category (e.g., Food, Transport, Utilities)

## Database Seeding

The `app/seed.py` script is used to populate the database with initial or sample data. This helps in:

- Setting up default categories or users
- Providing test data for development and testing
- Quickly initializing the database with meaningful records

To run the seed script:

```bash
python app/seed.py

## Expense Service

The `app/services/expense_service.py` module contains business logic related to expenses, including:

- Adding new expenses to the database
- Validating and processing expense data
- Acting as an intermediary between the API routes and the database models

This service layer helps keep the code modular, maintainable, and easier to test by separating core logic from request handling.

---

## Static Assets

The `app/static/` directory contains all frontend static files, including:

- **CSS stylesheets** for layout and design  
- **JavaScript files** for client-side interactivity and dynamic behavior  
- **Images and icons** used throughout the application  

These assets support the user interface and enhance user experience on the frontend.


## Expenses Management API

- **GET /expenses**  
  Fetch all expenses for the authenticated user, including metadata and optional receipt URLs.

- **POST /expenses**  
  Create a new expense entry with support for uploading receipt files (PNG, JPG, JPEG, PDF).  
  Validates input data, stores receipts securely, and returns the created expense with its receipt URL.

This feature enhances expense tracking by enabling users to attach and access digital receipts seamlessly.

## Expense Model Update: Receipt Upload Support
The Expense model now includes a new optional field receipt_url to store URLs of uploaded receipt files (e.g., images, PDFs). This enhancement allows users to associate digital receipts with their expense records for easier verification and tracking.

- **Field: receipt_url (string, nullable)

- **Purpose: Store the path or URL to uploaded receipt files linked to each expense

- ** Supported file types: PNG, JPG, JPEG, PDF
