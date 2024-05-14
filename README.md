# Flask Blog Project

## Introduction

This is a simple blog application built using Flask, a lightweight WSGI web application framework in Python. The application allows users to register, log in, create posts, edit posts, delete posts, and comment on posts.

## Tech Stack

- **Python**: The programming language used for the backend logic.
- **Flask**: The web framework used to build the application.
- **Flask-SQLAlchemy**: An extension for Flask that adds support for SQLAlchemy, an ORM (Object Relational Mapper).
- **Flask-Bcrypt**: An extension for Flask that provides bcrypt hashing utilities for password hashing.
- **Flask-Login**: An extension for Flask that provides user session management.
- **Flask-WTF**: An extension for Flask that integrates WTForms, which provides form rendering, validation, and CSRF protection.

## Project Structure

```
flask_blog/
    ├── app.py            # Entry point for running the application
    ├── __init__.py       # Initializes the Flask application and its extensions
    ├── routes.py         # Contains the route definitions and view functions
    ├── models.py         # Defines the database models
    ├── forms.py          # Defines the WTForms forms used in the application
    ├── templates/        # Contains HTML templates
    │   ├── layout.html
    │   ├── home.html
    │   ├── login.html
    │   ├── register.html
    │   ├── post.html
    │   └── single_post.html
    ├── static/           # Contains static files (e.g., CSS)
    │   └── style.css
    └── venv/             # Virtual environment directory (should be in .gitignore)
```

## Running the Project in VS Code on Windows

### Prerequisites

- Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/).
- Ensure you have VS Code installed. You can download it from [code.visualstudio.com](https://code.visualstudio.com/).

### Steps to Run

1. **Clone the Repository**:
   If you haven't cloned the repository yet, clone it using:

   ```sh
   git clone <repository_url>
   ```

2. **Open the Project in VS Code**:
   Open VS Code and use `File -> Open Folder...` to open the `flask_blog` project folder.

3. **Create and Activate the Virtual Environment**:
   Open the integrated terminal in VS Code (`View -> Terminal`) and run the following commands:

   ```sh
   python -m venv venv
   venv\Scripts\activate
   ```

4. **Install Dependencies**:
   With the virtual environment activated, install the necessary dependencies:

   ```sh
   pip install flask flask_sqlalchemy flask_bcrypt flask_login flask_wtf wtforms
   ```

5. **Initialize the Database**:
   Initialize the database by running the following commands in the terminal:

   ```sh
   set PYTHONPATH=.
   python
   ```

   In the Python interactive shell, run:

   ```python
   from __init__ import db
   db.create_all()
   exit()
   ```

6. **Run the Flask Application**:
   Run the application using:

   ```sh
   python app.py
   ```

7. **Open the App in a Browser**:
   Open your web browser and go to `http://127.0.0.1:5000/` to see your Flask app in action.

### Additional Notes

- Ensure your `PYTHONPATH` is set correctly to recognize the package structure.
- If you encounter any issues, check the terminal output for error messages and resolve any missing dependencies or incorrect paths.
