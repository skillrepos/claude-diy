"""Creates notes.db with made-up users and notes. Only needed if you want to run the app."""
import sqlite3

conn = sqlite3.connect("notes.db")
conn.executescript(
    """
    DROP TABLE IF EXISTS users;
    DROP TABLE IF EXISTS notes;
    CREATE TABLE users (id INTEGER PRIMARY KEY, username TEXT, email TEXT, password TEXT);
    CREATE TABLE notes (id INTEGER PRIMARY KEY, owner_id INTEGER, title TEXT, body TEXT);
    INSERT INTO users (username, email, password) VALUES
        ('maya', 'maya@example.com', 'blueberry-pancakes'),
        ('omar', 'omar@example.com', 'kettle-corn-42');
    INSERT INTO notes (owner_id, title, body) VALUES
        (1, 'Sprint goals', 'Ship the sharing feature.'),
        (2, 'Vendor list', 'Ask about the new laptops.');
    """
)
conn.commit()
print("notes.db created with 2 sample users and 2 notes")
