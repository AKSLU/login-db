from flask import Flask, request, render_template
import psycopg2

app = Flask(__name__)

conn = psycopg2.connect(
    dbname="base",
    user="postgres",
    password=" ",
    host="localhost"
)
cur = conn.cursor()

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        u = request.form['username']
        p = request.form['password']
        cur.execute("SELECT * FROM users WHERE username=%s AND password=%s", (u, p))
        if cur.fetchone():
            return render_template('welcome.html', username=u)
        else:
            return render_template('error.html')
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)


