from cgitb import html
from flask import Flask, render_template, request, redirect
from config import db 
from models import User

app = Flask(__name__)

@app.route('/')
def index():
    return "Welcome to flask app"

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "GET":
        return render_template("login.html")
    else:
        username = request.form['username']
        password = request.form['password']
        
        if db.users.find_one({"username": username, "password": password}):
            return "Login success"

        return redirect('/register')


@app.route('/register')
def register():
    #TODO: 
    # If req is get -> return register.html
    # else -> parse request object, 
    # if username is in db:
    #     redirect to login
    # else:  save user details into db
    # show a success message
    
    
    return "You are in register page"

@app.route('/homepage')
def homepage():
    return "Welcome to homepage"

@app.route('/weather')
def get_weather():
    return "Weather info"

if __name__=="__main__":
    print("executing main block")
    app.run(port=3000)

