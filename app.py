from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Vulnerable login function (SQL injection prone)
def unsafe_login(username, password):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
    cursor.execute(query)
    user = cursor.fetchone()
    conn.close()
    return user is not None

# Secure login function (parameterized queries)
def safe_login(username, password):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    user = cursor.fetchone()
    conn.close()
    return user is not None

@app.route('/', methods=['GET', 'POST'])
def login():
    message = ""
    login_success = False
    
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        mode = request.form['mode']
        
        if mode == 'unsafe':
            if unsafe_login(username, password):
                message = " Login SUCCESSFUL (Vulnerable Mode)"
                login_success = True
            else:
                message = " Login FAILED (Vulnerable Mode)"
        else:
            if safe_login(username, password):
                message = " Login SUCCESSFUL (Secure Mode)"
                login_success = True
            else:
                message = " Login FAILED (Secure Mode)"
    
    return render_template('login.html', message=message, login_success=login_success)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)