from flask import Flask, render_template, request, redirect
import sqlite3
from datetime import datetime
import bcrypt

app = Flask(__name__)


def init_db():
    with sqlite3.connect('database.db') as conn:
        print(f"\033[93mTrying to create new table if not already created:\033[00m")
        conn.execute('''
            CREATE TABLE IF NOT EXISTS confessions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                confession TEXT NOT NULL,
                password TEXT NOT NULL, 
                date DATE NOT NULL
            )
        ''')
        print(f"\033[92mTable confessions is ready for use:\033[00m")
        conn.commit()


def checkid(id):
    try:
        confessions = sqlite3.connect("database.db")
        cursor = confessions.cursor()
        cursor.execute('SELECT id FROM confessions')
        ids = [str(row[0]) for row in cursor.fetchall()]
        confessions.commit()
        if id not in ids:
            return False
        return True
    except sqlite3.Error as e:
        print(f"\033[91mAn error occurred:\033[00m {e} ")
        init_db()
        return None
    finally:
        if confessions:
            confessions.close()


@app.route('/home', methods=['GET'])
@app.route('/', methods=['GET'])
def home():
    try:
        confessions = sqlite3.connect("database.db")
        cursor = confessions.cursor() 
        cursor.execute('SELECT * FROM confessions') 
        data = cursor.fetchall()
        confessions.commit()
    except sqlite3.Error as e:
        print(f"\033[91mAn error occurred:\033[00m {e} ")
        init_db()
    finally:
        if confessions:
            confessions.close()
    return render_template('index.html', data=data)


@app.route('/AboutMe', methods=['GET'])
def About_Me():
    return render_template('About-Me.html')


@app.route('/PostYourConfession', methods=['GET', 'POST'])
def Post_Confession():
    if request.method == 'POST': 
        title = request.form['title'] 
        confession = request.form['confession']
        password = request.form['password'].encode('utf-8')
        password = bcrypt.hashpw(password, bcrypt.gensalt())
        if title == "" or confession == "" or password == "":
            return redirect("/", code=302)
        try:
            confessions = sqlite3.connect("database.db")
            cursor = confessions.cursor()
            cursor.execute("INSERT INTO confessions (title, confession,password, date) VALUES (?, ?, ?, ?)", (title, confession, password, datetime.now().strftime('%d/%m/%Y %I:%M:%S %p'))) 
            confessions.commit()
        except sqlite3.Error as e:
            print(f"\033[91mAn error occurred:\033[00m {e} ")
            init_db()
        finally:
            if confessions:
                confessions.close()
        return redirect("/", code=302)
    else:
        return render_template('PostConfession.html')


@app.route('/delete', methods=['GET', 'POST'])
@app.route('/delete/<id>', methods=['GET', 'POST'])
def delete_confession(id=None):
    idcheck = checkid(id)
    if idcheck == False or idcheck == None or id == None:
        return redirect("/", code=302)
    if request.method == 'POST':
        enterd_password = request.form['password'].encode('utf-8')
        try:
            confessions = sqlite3.connect("database.db")
            cursor = confessions.cursor()
            cursor.execute('SELECT password FROM confessions WHERE id=?', (id,))
            password = cursor.fetchone()
            confessions.commit()
            if password and bcrypt.checkpw(enterd_password, password[0]):
                cursor.execute('DELETE FROM confessions WHERE id=?', (id,))
                confessions.commit()
                return redirect("/", code=302)
            else:
                return render_template("delete_confession.html", error_code="Password incorrect try again")
        except sqlite3.Error as e:
            print(f"\033[91mAn error occurred:\033[00m {e} ")
            init_db()
        finally:
            if confessions:
                confessions.close()
    else:
        return render_template("delete_confession.html", error_code="")


@app.route('/confession', methods=['GET'])
@app.route('/confession/<id>', methods=['GET'])
def seeing_confession(id=None):
    idcheck = checkid(id)
    if idcheck == False or idcheck == None or id == None:
        return redirect("/", code=302)
    else:
        try:
            confessions = sqlite3.connect("database.db")
            cursor = confessions.cursor() 
            cursor.execute('SELECT * FROM confessions WHERE id=?', (id,)) 
            confession = cursor.fetchone()
            confessions.commit()
        except sqlite3.Error as e:
            print(f"\033[91mAn error occurred:\033[00m {e} ")
            init_db()
        finally:
            if confessions:
                confessions.close()
        return render_template("confession.html", confession=confession)


@app.route('/<nothing>', methods=['GET'])
def Handling_nothing(nothing):
    return render_template('Nothing.html', nothing=nothing)


if __name__ == '__main__':
    init_db()
    app.run(debug=True, host="0.0.0.0", port=80)
