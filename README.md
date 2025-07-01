# SQL Injection Demonstration 

A Flask-based educational tool that showcases SQL injection vulnerabilities and prevention techniques

# Key Features

1. Interactive toggle between vulnerable and secure modes

2. Real-time demonstration of SQL injection attacks

3. Visual feedback on login success/failure

4. Clean, responsive web interface

5. Complete prevention using parameterized queries

# Requirements

Python 3.6+

Flask web framework

SQLite database (built-in with Python)

      bash

      pip install flask

# Setup Guide
1. Clone Repository

      bash
   
      git clone https://github.com/rohitharumugam22/sql_injection.git

      cd sql_injection
   
3. Initialize Database

      bash

      python init_db.py
   
Creates database.db with sample users:

Username    Password

Rohith    rohith2006

Vignesh    vicky2005

Udhaya    vada2006

4. Run Application

      bash
   
      python app.py
   
5. Access Interface

Visit in your browser:

    http://localhost:5000

# Demonstration Guide
Vulnerable Mode (SQL Injection Works)
Select "Vulnerable Mode" tab

Enter:
Username: ' OR '1'='1' --
Password: anything (or leave blank)

Click Login

Result: Login successful! 🟢

Secure Mode (SQL Injection Prevented)
Select "Secure Mode" tab

Use same credentials:
Username: ' OR '1'='1' --
Password: anything

Click Login

Result: Login failed! 🔴

# How It Works
Vulnerable Code

python

UNSAFE: String concatenation
query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
cursor.execute(query)

Secure Code

python

SAFE: Parameterized queries
cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))

# Project Structure

text

sql-injection/

├── app.py                 # Main Flask application

├── init_db.py             # Database initialization script

├── database.db            # SQLite database fill

└── templates/
    
    └── login.html         # Login page template
