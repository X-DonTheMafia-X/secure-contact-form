## Secure Contact App

A secured Flask web application designed for small business who want to collect online orders from their customer or a student who is willing to learn a real life full stack web development example.

This application collects customer inquires or orders, send them confirmation email and notify the admin, stores them in a database which can be accessed by an admin viewer in a protected administrative dashbord.

This app is designed while keeping security in mind and applying real life defenses including authentication, authorization, CSRF protection, input validation, rate limiting, secure file handlings, password hashing, and audit logging.

## How to setup

Requirements:
- install python 3
- install VS code
- install git bash

Before you go further make sure to use a virtual environment to prevent conflicts and download all the required files in requirements.txt file before proceeding.

step 1: Open this folder in bash and activate your Virtual Environment (Windows: source .venv/Scripts/activate Linux: source .venv/bins/activate)

step 2: Rename secure-contact-app/.env.example to .env

step 3: Fill your own environment variable and save it, now open your bash in the root folder of this project and type:
- flask migrate -m "Initial Migration"
- flask db upgrade

step 4: open bash and enter:
                            python run.py to test the application
                            login username and password for admin: admin and Ba911nana
                            login username and password for jessica: Jessica and jessi123

step 5: If you want to set you own admin and users:
open bash, and type:
- flask shell
- from app.extensions import db
- from app.models.user import User
- User.query.delete()
- db.session.commit()
- exit() to exit the terminal

step 6: Now you deleted the existing users, we need you set up a new users.
open flash shell
- from app.extensions import  db
- from app.models.user import User

- admin = User(username="admin", role="admin")
- admin.set_password("your-password-here")
- db.session.add(admin)
- db.session.commit()

Do the same for user = ... only the difference is you put role="user"

step 7: Now, to make it your own shop website you need make some changes to it's appearings
- go to app/services/email_service.py and replace YOUR BUSINESS NAME with yours
- go to app/templates/base/base.html and make same changes
- got to app/templates/pages/home.html, app/templates/components/footer.html and navbar.html, and make necessary changes as per your requirement

## Features

### Customer Features

- Contact/submission form
- Server-side form validation
- CSRF protection
- Email confirmation after submission
- Optional file attachment support
- User-friendly validation and error messages
- Secure handling of uploaded files

### Administrative Features

- Protected administrator login
- Password-hashed administrator credentials
- Authenticated submission management
- Submission viewing and deletion
- Secure document downloads
- Audit/security event logging
- Login protection and rate limiting

### Security Features

- Password hashing
- CSRF protection
- Authentication with Flask-Login
- Authorization and role-based access control
- Server-side input validation
- Rate limiting
- Secure file-upload handling
- Filename sanitization
- UUID-based uploaded filenames
- HTTP-only session cookies
- SameSite cookie configuration
- Secure cookie configuration for production
- Security/audit logging
- Controlled error handling
- Environment-based configuration
- Automated testing

---

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Application programming language |
| Flask | Web framework |
| Flask-SQLAlchemy | Database ORM |
| Flask-Migrate | Database migrations |
| Flask-Login | Authentication and session management |
| Flask-WTF | Forms and CSRF protection |
| Flask-Mail | Email delivery |
| SQLite | Development database |
| PostgreSQL | Production database |
| Pytest | Automated testing |
| HTML/CSS/JavaScript | Frontend |
| Git/GitHub | Version control |
| Render | Production deployment |

---

## Project Structure

```text
secure-contact-app/
│
├── app/
│   ├── routes/
│   │   ├── main.py
│   │   ├── auth.py
│   │   ├── admin.py
│   │   ├── downloads.py
│   │   └── errors.py
│   │
│   ├── models/
│   │   ├── user.py
│   │   ├── submission.py
│   │   └── audit_log.py
│   │
│   ├── forms/
│   │   └── contact_form.py
│   │
│   ├── services/
│   │   ├── submission_service.py
│   │   ├── email_service.py
│   │   ├── upload_service.py
│   │   ├── download_service.py
│   │   └── audit_service.py
│   │
│   ├── security/
│   │   └── ...
│   │
│   ├── templates/
│   │   ├── base/
│   │   ├── components/
│   │   ├── admin/
│   │   └── ...
│   │
│   ├── static/
│   │   ├── css/
│   │   ├── js/
│   │   └── images/
│   │
│   ├── extensions.py
│   └── __init__.py
│
├── tests/
│   ├── 
│   ├── 
│
├── migrations/
├── docs/
│
├── .env.example
├── .gitignore
├── config.py
├── requirements.txt
├── run.py
└── README.md

