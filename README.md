# User Management API

This is a user management system API built with Django and Django Rest Framework. The API supports user registration, login, and the management of a custom user model.

## Features

- User registration and login.
- Custom user model with fields like `first_name`, `last_name`, and `email`.
- User profiles and permissions management.

## Requirements

- Python 3.9 or higher
- Django 3.2 or higher
- Django Rest Framework

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/usermanagement.git
```

### 2. Install dependencies
```bash
cd usermanagement
python -m venv venv
source venv/bin/activate  # On Windows use venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Apply database migrations
```bash
python manage.py makemigrations
python manage.py migrate
```
### 4. Create a superuser
```bash
python manage.py createsuperuser
```
5. Run the development server
```bash
python manage.py runserver
```
6. API Endpoints
POST /register/: Register a new user.

Request body:
```json
{
  "username": "dhruv",
  "email": "dhruv@example.com",
  "password": "password123",
  "phone_number": "1234567890"
}
```
Response:
```json
{
  "message": "User created successfully."
}

```
POST /login/: Login to get a JWT token.

Request body:
```json
{
  "email": "dhruv@example.com",
  "password": "password123"
}

```
Response:
```json
{
  "token": "jwt_token_here"
}
```
GET /profile/: Get the current user's profile (requires JWT authentication).

Response:
```json
{
  "username": "dhruv",
  "email": "dhn@example.com",
  "phone_number": "1234567890"
}
```
