from flask import Flask, render_template, request
import sqlite3
app = Flask(__name__)

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

@app.route('/addposts', methods=['GET', 'POST'])
def addposts():
    if request.method == 'POST':
        c = request.form.get("Title")
        d = request.form.get("Content")
        conn = get_db_connection()
        print(c,"------------------------------------------------------------")
        query = "INSERT INTO posts (title, content) VALUES (?, ?)"
        cursor = conn.execute(query, (c, d))
        conn.commit()
        # conn.close()
        return render_template('addposts3.html', posts="Post successfully added to the DB")
    else:
        return render_template('addposts3.html')

if __name__ == "__main__":
    app.run(debug=True, port=8000)

