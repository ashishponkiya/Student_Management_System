# MySQL Setup Guide for Student Management System

## Step 1: Install MySQL Server
If you haven't installed MySQL yet, download and install it from:
https://dev.mysql.com/downloads/mysql/

## Step 2: Create Database

Open MySQL Command Line or MySQL Workbench and run:

```sql
CREATE DATABASE studentmgm;
```

## Step 3: Verify Connection Credentials

Check your MySQL credentials:
- **Host**: localhost
- **Port**: 3306
- **User**: root (or your username)
- **Password**: (your password)

If your credentials are different, update them in `studentmgm/settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'studentmgm',
        'USER': 'your_mysql_user',  # Change this
        'PASSWORD': 'your_mysql_password',  # Change this
        'HOST': 'localhost',
        'PORT': '3306',
        'OPTIONS': {
            'charset': 'utf8mb4',
        }
    }
}
```

## Step 4: Run Migrations

After updating settings and creating the database, run:

```bash
python manage.py migrate
```

This will create all the necessary tables in your MySQL database.

## Step 5: Create Superuser (Optional)

To access Django admin panel:

```bash
python manage.py createsuperuser
```

## Step 6: Run Development Server

```bash
python manage.py runserver
```

Your application will now use MySQL instead of SQLite!

## Troubleshooting

**Error: "Access denied for user 'root'@'localhost'"**
- Check if your MySQL username and password are correct
- Update them in `settings.py`

**Error: "Can't connect to MySQL server"**
- Make sure MySQL server is running
- Check if the host and port are correct

**Error: "mysqlclient not installed"**
- Run: `pip install mysqlclient`
