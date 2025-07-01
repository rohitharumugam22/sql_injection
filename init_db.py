import sqlite3

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# Create users table
cursor.execute('''
CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    password TEXT NOT NULL
)
''')

# Add sample users
users = [
    ('Rohith', 'rohith2006'),
    ('Vignesh', 'vicky2005'),
    ('Udhaya', 'vada2006')
]
cursor.executemany("INSERT INTO users (username, password) VALUES (?, ?)", users)

conn.commit()
conn.close()
print("Database initialized successfully!")