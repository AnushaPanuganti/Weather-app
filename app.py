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


@app.route('/register',methods=['GET', 'POST'])
def register():
    #TODO: 
    # If req is get -> return register.html
    if request.method == "GET":
        return render_template("register.html")
    # else -> parse request object, 
    else:
        username = request.form['username']
        password = request.form['set password']
        # if username is in db:
        if db.users.find_one({"username": username}):
            print("user already exists")
            return redirect('/login')

        #     redirect to login
        # else:  save user details into db
        else:
            db.users.insert_one({"username": username, "password": password})
        # show a success message
            return 'Registered successfully,<a href= "/login" >Click here to login</a>'

@app.route('/homepage')
def homepage():
    return "Welcome to homepage"

@app.route('/weather')
def get_weather():
    return "Weather info"

if __name__=="__main__":
    print("executing main block")
    app.run(port=3000)

