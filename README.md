# Expense Tracker

A full-stack personal expense tracking application with a FastAPI backend and a plain HTML/CSS/JS frontend. No frontend build tools required.

---

## Features

- User registration and login with JWT authentication
- Argon2 password hashing (with SHA-256 pre-hashing to protect full password length)
- Add, edit, and delete expenses
- Filter expenses by category and search by keyword
- Live spending breakdown bar showing category proportions
- Monthly spend summary
- Single-file HTML frontend — no Node.js, no build step

---

## Project Structure

```
expense_tracker/
├── app/
│   ├── __init__.py
│   ├── main.py              # FastAPI app, middleware, router registration
│   ├── core/
│   │   ├── config.py        # Settings loaded from .env
│   │   ├── database.py      # SQLAlchemy engine, session, Base
│   │   └── security.py      # Argon2 hashing, JWT creation and decoding
│   ├── models/
│   │   ├── user.py          # User database model
│   │   └── expense.py       # Expense database model
│   ├── schemas/
│   │   ├── user.py          # Pydantic schemas for users and tokens
│   │   └── expense.py       # Pydantic schemas for expenses
│   ├── crud/
│   │   ├── user.py          # User database operations
│   │   └── expense.py       # Expense database operations
│   └── routers/
│       ├── auth.py          # /auth/register, /auth/login, get_current_user
│       ├── users.py         # /users/me
│       └── expenses.py      # Full CRUD for expenses
├── static/
│   └── index.html           # Frontend (plain HTML/CSS/JS)
├── .env                     # Environment variables (never commit this)
├── .env.example             # Template for .env
├── .gitignore
└── requirements.txt
```

---

## Requirements

- Python 3.10+
- pip
- Termux (if running on Android) or any Linux/macOS terminal

---

## Setup

### 1. Clone or copy the project

If working in Termux, make sure the project is in Termux home — **not** in shared storage (`/storage/emulated/0/`), as Android's shared filesystem does not support the operations Python and pip need.

```bash
cd ~
# project should be at ~/expense_tracker
```

### 2. Install dependencies

```bash
cd ~/expense_tracker
pip install -r requirements.txt
```

### 3. Create your `.env` file

```bash
cp .env.example .env
```

Then open `.env` and set a strong `SECRET_KEY`:

```
DATABASE_URL=sqlite:///./expense_tracker.db
SECRET_KEY=replace-this-with-a-long-random-string
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=60
```

You can generate a secure key with:

```bash
python -c "import secrets; print(secrets.token_hex(32))"
```

### 4. Run the server

```bash
uvicorn app.main:app --reload
```

The API will be available at `http://127.0.0.1:8000`.

---

## Accessing the Frontend

The frontend is served directly by FastAPI as a static file. Once the server is running, open your browser and go to:

```
http://127.0.0.1:8000/static/index.html
```

No separate frontend server needed.

---

## API Endpoints

All endpoints are prefixed with `/api/v1`.

### Auth

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/auth/register` | Create a new user account |
| POST | `/auth/login` | Login and receive a JWT access token |

### Users

| Method | Endpoint | Description | Auth required |
|--------|----------|-------------|---------------|
| GET | `/users/me` | Get current user's profile | ✓ |

### Expenses

| Method | Endpoint | Description | Auth required |
|--------|----------|-------------|---------------|
| POST | `/expenses/` | Create a new expense | ✓ |
| GET | `/expenses/` | List all expenses (supports pagination) | ✓ |
| GET | `/expenses/{id}` | Get a single expense | ✓ |
| PUT | `/expenses/{id}` | Update an expense | ✓ |
| DELETE | `/expenses/{id}` | Delete an expense | ✓ |

All expense endpoints are scoped to the logged-in user. A user cannot access or modify another user's expenses.

Interactive API docs are available at `http://127.0.0.1:8000/docs` while the server is running.

---

## Security Notes

- Passwords are SHA-256 pre-hashed before being passed to Argon2. This ensures the full password is always hashed, regardless of length, since Argon2 (like bcrypt) has an input length limit.
- The `SECRET_KEY` in `.env` signs all JWT tokens. Keep it secret and never commit it to version control.
- The `.gitignore` excludes `.env` and the SQLite database file.
- Expense queries always filter by both `id` and `user_id`, so users cannot access each other's data even if they guess an expense ID.

---

## Database

The app uses SQLite by default, which requires no additional setup. The database file (`expense_tracker.db`) is created automatically in the project root on first run.

To switch to PostgreSQL or MySQL, update `DATABASE_URL` in `.env`:

```
DATABASE_URL=postgresql://user:password@localhost/expense_tracker
```

No code changes are needed — SQLAlchemy handles the rest.

---

## Development Notes

- Built and tested in Termux on Android
- All development done from `~/` (Termux home), not shared storage
- Reload (`--reload`) flag is useful during development but should be removed in production
- CORS is currently set to `allow_origins=["*"]` — restrict this to your actual frontend origin before deploying

---

## Tech Stack

| Layer | Technology |
|-------|------------|
| Backend framework | FastAPI |
| Database ORM | SQLAlchemy |
| Database | SQLite (default) |
| Password hashing | Argon2 via passlib |
| Authentication | JWT via python-jose |
| Data validation | Pydantic v2 |
| Frontend | Plain HTML, CSS, JavaScript |
| Server | Uvicorn |
# Expense-tracker-App
# Expense-tracker-App
# Expense-tracker-App
