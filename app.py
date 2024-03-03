from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

conn = sqlite3.connect("users.db", check_same_thread=False)
cursor = conn.cursor()

  
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    username TEXT,
    password TEXT
)

""")

conn.commit()
test_user = ("Test", "Test")
cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", test_user)
conn.commit()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    cursor.execute(query)
    user = cursor.fetchone()

    if user:
        return redirect(url_for("flag"))
    else:
        return render_template("index.htmln", message="Invalid credentials")

@app.route("/flag")
def flag():
    return render_template("flag.html")

