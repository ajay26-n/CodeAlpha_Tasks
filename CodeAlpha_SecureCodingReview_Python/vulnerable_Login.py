from flask import Flask, request
import sqlite3

app = Flask(__name__)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return '''
        <h2>Vulnerable Login Page</h2>
        <form method="POST">
            Username: <input type="text" name="username"><br><br>
            Password: <input type="text" name="password"><br><br>
            <input type="submit" value="Login">
        </form>
        '''


    username = request.form['username']
    password = request.form['password']

    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    
    query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
    print("Executing query:", query)   

    cursor.execute(query)
    result = cursor.fetchone()

    conn.close()

    if result:
        return "Login Successful (INSECURE)"
    else:
        return "Login Failed"

if __name__ == "__main__":
    app.run(debug=True)