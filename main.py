from flask import Flask, render_template,request,redirect,session
import mysql.connector
import os

app=Flask(__name__)
app.secret_key=os.urandom(24)


@app.route('/')
def login():
    return render_template('login.html')

@app.route('/register')
def about():
    return render_template('register.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/login_validation', methods=['POST'])
def ligin_validation():
    email=request.form.get('email')
    password=request.form.get('password')
    return"The email is {} and the password is {}".format(email,password)

@app.route('/add_user', methods=['POST'])
def add_user():
    name=request.form.get('uname')
    email=request.form.get('uemail')
    password=request.form.get('upassword')
    confirm_password=request.form.get('confirm_password')

    cursor.execute("""INSERT INTO 'users'('user_id', 'name', 'email', 'password','confirm-password) VALUES(NULL,'{}','{}','{}','{}') """.format(name,email,password, confirm_password))
    conn.commit()
    return "user registered successfully"
if __name__=="__main__":
    app.run(debug=True)