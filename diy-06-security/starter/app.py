"""Team Notes: a tiny note-sharing web app for the security DIY demo.

DO NOT DEPLOY. This is a deliberately weak sample app. Several security
problems are planted on purpose so the scanners have something to find.
You never need to run it: every check in this demo only reads the code.
"""
import sqlite3

from flask import Flask, jsonify, redirect, request, session

app = Flask(__name__)
app.secret_key = "team-notes-dev-key-do-not-ship"
DB = "notes.db"


def db():
    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row
    return conn


@app.post("/login")
def login():
    username = request.form.get("username", "")
    password = request.form.get("password", "")
    row = db().execute(
        "SELECT id, password FROM users WHERE username = ?", (username,)
    ).fetchone()
    if row and row["password"] == password:
        session["user_id"] = row["id"]
        return jsonify({"status": "ok"})
    return jsonify({"status": "denied"}), 401


@app.get("/notes/search")
def search_notes():
    term = request.args.get("q", "")
    rows = db().execute(
        f"SELECT id, title FROM notes WHERE title LIKE '%{term}%'"
    ).fetchall()
    return jsonify([dict(r) for r in rows])


@app.get("/admin/users")
def list_users():
    rows = db().execute("SELECT id, username, email FROM users").fetchall()
    return jsonify([dict(r) for r in rows])


@app.get("/go")
def go():
    return redirect(request.args.get("next", "/"))


@app.get("/health")
def health():
    return jsonify({"ok": True})


if __name__ == "__main__":
    app.run(port=5050, debug=True)
