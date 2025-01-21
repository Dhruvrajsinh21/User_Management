# User Management API

This is a user management system API built with Django and Django Rest Framework. The API supports user registration, login, and the management of a custom user model.

## Features

- User registration and login.
- User profiles and permissions management.

POSTMAN TESTING:

![image](https://github.com/user-attachments/assets/89bb4323-a5e1-40d4-8ccc-3117c0427bf6)
![image](https://github.com/user-attachments/assets/49618a42-2a0e-4efc-bfc4-578186b87d09)
![image](https://github.com/user-attachments/assets/fac1c6a8-6e7f-4fee-aba7-e70d43b26aa5)
![image](https://github.com/user-attachments/assets/b131920b-b202-45c3-8772-736dfa5ea0a2)






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
