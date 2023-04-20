from flask import Flask, render_template, request
import sqlite3
app = Flask(__name__)
# Understanding 1: Database database.db file is the database
# 2: "/" is displaying sql query that displays all posts in db. Is this GET method?
# 3: Want to insert a new blog post. So i will create a new function with new decorator and new html.
#    this will be a POST method with INSERT query?
def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM posts').fetchall()
    conn.close()
    return render_template('index2.html', posts=posts)

@app.route('/addposts')
def addposts():
    conn = get_db_connection()
    #table name is "posts". How to add values captured in HTML page?
    query = "INSERT INTO posts (title, content) VALUES (%s, %s, %s)"
    newposts = conn.execute(query).fetchall()
    conn.close()
    return render_template('addposts2.html', posts="Post successfully added to the DB")


if __name__ == "__main__":
    app.run(debug=True, port=8000)

