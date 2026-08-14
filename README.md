# Secure Contact App

A security-focused Flask web application built for small businesses that want to collect online orders or inquiries from customers — and a great hands-on reference for anyone learning full-stack web development.

The app collects customer inquiries or orders, sends confirmation emails, notifies the admin, and stores submissions in a database accessible through a protected administrative dashboard.

Security is a first-class concern throughout: authentication, authorization, CSRF protection, input validation, rate limiting, secure file handling, password hashing, and audit logging are all built in.

---

## Table of Contents

- [Features](#features)
- [Technology Stack](#technology-stack)
- [Project Structure](#project-structure)
- [Setup](#setup)
- [Testing on Your Phone](#testing-on-your-phone)
- [Customizing Users](#customizing-users)
- [Making It Your Own](#making-it-your-own)

---

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

| Technology            | Purpose                                |
|------------------------|-----------------------------------------|
| Python                 | Application programming language        |
| Flask                  | Web framework                            |
| Flask-SQLAlchemy       | Database ORM                             |
| Flask-Migrate          | Database migrations                      |
| Flask-Login            | Authentication and session management    |
| Flask-WTF              | Forms and CSRF protection                |
| Flask-Mail             | Email delivery                           |
| SQLite                 | Development database                     |
| PostgreSQL             | Production database                      |
| Pytest                 | Automated testing                        |
| HTML/CSS/JavaScript    | Frontend                                 |
| Git/GitHub             | Version control                          |
| Render                 | Production deployment                    |

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
```

---

## Setup

### Requirements
- [Python 3](https://www.python.org/downloads/)
- [VS Code](https://code.visualstudio.com/)
- [Git Bash](https://git-scm.com/downloads)

Before proceeding, create and activate a virtual environment to avoid dependency conflicts, then install everything listed in `requirements.txt`.

### Step 1 — Set up your environment

Open this folder in Bash and activate your virtual environment:

```bash
# Windows
source .venv/Scripts/activate

# Linux / macOS
source .venv/bin/activate
```

Then install dependencies:

```bash
pip install -r requirements.txt
```

### Step 2 — Configure environment variables

Rename `secure-contact-app/.env.example` to `.env`, then fill in your own values and save.

### Step 3 — Run database migrations

From the project root:

```bash
flask db migrate -m "Initial Migration"
flask db upgrade
```

### Step 4 — Run the app

```bash
python run.py
```

Default login credentials for testing:

| Role  | Username | Password  |
|-------|----------|-----------|
| Admin | `admin`  | `Ba911nana` |
| User  | `Jessica`| `jessi123`  |

> ⚠️ **Change these default credentials before deploying anywhere beyond your local machine.**

---

## Testing on Your Phone

1. Start the app so it's reachable on your local network:

   ```bash
   flask run --host=0.0.0.0
   ```

2. Find your computer's local IP address:

   ```bash
   ipconfig
   ```

3. On your phone (connected to the same Wi-Fi network), open a browser and visit:

   ```text
   http://<your_ip_address>:5000
   ```

---

## Customizing Users

### Remove the existing sample users

```bash
flask shell
```

```python
from app.extensions import db
from app.models.user import User

User.query.delete()
db.session.commit()
exit()
```

### Create your own users

```bash
flask shell
```

```python
from app.extensions import db
from app.models.user import User

# Admin account
admin = User(username="admin", role="admin")
admin.set_password("your-password-here")
db.session.add(admin)
db.session.commit()

# Regular user account (repeat as needed, with role="user")
user = User(username="your-username", role="user")
user.set_password("your-password-here")
db.session.add(user)
db.session.commit()
```

---

## Making It Your Own

To turn this into your own shop's website:

1. **Business name** — update it in:
   - `app/services/email_service.py`
   - `app/templates/base/base.html`
2. **Branding & content** — update as needed in:
   - `app/templates/pages/home.html`
   - `app/templates/components/footer.html`
   - `app/templates/components/navbar.html`
