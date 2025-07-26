**Project Overview:**

The "automated-employee-system" project is a small employee management system built on Flask, SQLAlchemy, and Flask-Login. Below is the detailed structure of the repository.

---

### 1. **Root Directory**

* **`main.py`** — This is the entry point for the application. The app is created by importing the app factory from the `app` package, and the web server is started here.
* **`config.py`** — This file contains all configurations, including the secret key, database URI (`app.db`), file upload configurations, and allowed extensions.
* **`create_admin.py`** — A helper script used to create the admin user: it connects to the app, checks if an admin user exists, and if not, creates one with a set password.
* **`bulk_add.py`** — A script that demonstrates how to create a context with `create_app()` and bulk add predefined employees to the database.
* **`requirements.txt`** — Lists dependencies like Flask, Flask-Login, Flask-WTF, Flask-SQLAlchemy, pandas, openpyxl, pdfkit, Werkzeug, matplotlib.
* **`app.db`** — SQLite database file.
* **`test.csv`** and **`text.txt`** — Sample data files that can be used to test data uploads.
* **`venv`** and **`__pycache__`** — Virtual environment and compiled files, not required to describe in README.

---

### 2. **`app/` Package**

* **`__init__.py`** — Implements the `create_app()` factory that initializes the Flask app, sets up extensions (`SQLAlchemy`, `LoginManager`, `CSRFProtect`), registers blueprints (`auth`, `views`), creates tables, and adds a default admin user on the first run.
* **`models.py`** — Defines the `User`, `Employee`, and `Task` classes. The `User` model stores username and password hash. The `Task` model links to the `Employee` and stores task completion time and percentage. The `Employee` model includes methods to calculate the number of tasks, average time, completion percentage, and total score.
* **`forms.py`** — Defines forms using Flask-WTF: login form (`LoginForm`), employee addition form with role selection, task addition form with time tracking, password change form, and deletion form.
* **`auth.py`** — Defines the `auth` blueprint and routes for authentication and employee management:

  * `login()` — Handles login with form validation and redirection.
  * `logout()` — Logs out the user.
  * `list_employees()` — Displays a list of employees and a deletion form.
  * `add_employee()` — Adds a new employee and creates a user account; available only to the admin.
  * `delete_employee()` — Deletes an employee and their user account.
  * `add_task()` — Adds tasks for employees; available to admins and managers.
  * `change_password()` — Allows users to change their passwords.
* **`views.py`** — Contains the main interface logic:

  * `dashboard()` — Displays the dashboard with metrics on employees, task counts, total time, completion percentage, and average ratings.
  * `reports()` — Generates a report, sorts employees by scores, and passes data to the `reports.html` template.
  * `export_csv()` — Exports employee scores to a CSV file with BOM for Excel compatibility.
  * `upload_data()` — Handles CSV file uploads, checks admin permissions, and creates new employees and tasks based on the uploaded data.
* **`templates/`** — Contains HTML templates:

  * `base.html` — Base layout.
  * `login.html` — Login form.
  * `add_employee.html`, `add_task.html`, `change_password.html` — Corresponding forms for adding employees, tasks, and changing passwords.
  * `employees.html` — Employee table.
  * `dashboard.html` — Dashboard displaying metrics.
  * `reports.html` — Report page.
  * `report.html` — Displays report data, including CSV export and other features.

---

### **Usage**

To run the application:

1. Clone the repository and navigate to the root directory.
2. Set up a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```
4. Configure your database and admin credentials in `config.py`.
5. To create an admin user, run:

   ```bash
   python create_admin.py
   ```
6. Start the application:

   ```bash
   python main.py
   ```
7. Navigate to `http://127.0.0.1:5000` to access the application.

---

This structure ensures a clear organization for managing employees, tasks, and user authentication using Flask. It’s easily extensible for future features such as more detailed reports or advanced user roles.
