from flask import Flask, render_template
import sqlite3

app = Flask(__name__)


def init_db():
    with sqlite3.connect('database.db') as conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS confessions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                confession TEXT, 
                date DATE
            )
        ''')
        print ("Table created successfully")
        conn.commit()


@app.before_request
def setup():
    init_db()


@app.route('/home')
@app.route('/')
def home():
    connect = sqlite3.connect('database.db') 
    cursor = connect.cursor() 
    cursor.execute('SELECT * FROM confessions') 
  
    data = cursor.fetchall()
    return render_template('index.html', data=data)

@app.route('/AboutMe')
def About_Me():
    return render_template('About-Me.html')


@app.route('/confession/<id>')
def Handling_confession_get(id):
    return "asd"


@app.route('/<nothing>')
def Handling_nothing(nothing):
    return render_template('Nothing.html', nothing=nothing)


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
