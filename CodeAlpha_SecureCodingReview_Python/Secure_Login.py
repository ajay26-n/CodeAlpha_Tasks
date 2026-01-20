from flask import Flask, request
import sqlite3
import hashlib

app = Flask(__name__)

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return '''
        <h2>Secure Login Page</h2>
        <form method="POST">
            Username: <input type="text" name="username"><br><br>
            Password: <input type="password" name="password"><br><br>
            <input type="submit" value="Login">
        </form>
        '''

    
    username = request.form['username']
    password = hash_password(request.form['password'])

    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    
    cursor.execute(
        "SELECT * FROM users WHERE username=? AND password=?",
        (username, password)
    )

    result = cursor.fetchone()
    conn.close()

    if result:
        return "Login Successful (SECURE)"
    else:
        return "Login Failed (SECURE)"

if __name__ == "__main__":
    app.run(debug=False)
