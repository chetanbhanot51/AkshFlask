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
        return render_template('index2.html', posts="lets see")
    return render_template('addposts3.html', posts="Post successfully added to the DB")
        # print("Post successfully added to the DB")
    # else:
    #     return render_template('addposts3.html')

@app.route('/delposts', methods=['GET', 'POST'])
def delposts():
    if request.method == 'POST':
        a = request.form.get('btn')
        conn = get_db_connection()
        print('---------------------------',a)
        query = "DELETE FROM POSTS WHERE id = ?"
        cursor = conn.execute(query,(a))
        conn.commit()
    return render_template('delposts.html', val=a)

global a
a = 0

@app.route('/editposts', methods=['GET', 'POST'])
def editposts():
    global a
    # print("-------------------------------->",a)
    if request.method == 'POST':
        if request.form.get('editbtn') != None:
            a = request.form['editbtn']
        if request.form.get('newbutton') !=None:
            new_content = request.form.get('newbutton')
            print(new_content,"********************************")
            conn = get_db_connection()
            print('---------------------------',a)
            query = "UPDATE posts SET content = ? WHERE  id = ?"
            conn.execute(query,(new_content, a))
            conn.commit()
            return render_template('editposts3.html')
            # return new_content
    return render_template('editposts.html')

if __name__ == "__main__":
    app.run(debug=True, port=8000)

