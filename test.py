from flask import Flask
from flask import render_template
import sqlite3

app = Flask(__name__)

conn = sqlite3.connect('bioinform.sqlite')
c = conn.cursor()
@app.route('/')
def Index():
    cur = c.execute('SELECT * FROM Bioinform')
    rows = cur.fetchall()
    return render_template('index.html', Bioinform=rows)


if __name__ == '__main__':
    app.run()
