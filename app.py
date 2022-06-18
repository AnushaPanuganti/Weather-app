from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return "Welcome to flask app"

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "GET":
        return render_template("login.html")
    else:
        print("login called with POST as method")
        username = request.form['username']
        print("username : ",username )

        #Todo: 
        # verify if username and password exists in the db
        # if exists: 
        #   redirect to homepage
        # else: 
        #   redirect to register

        return 'received username:'+username

@app.route('/register')
def register():
    pass

@app.route('/homepage')
def homepage():
    return "Welcome to homepage"

@app.route('/weather')
def get_weather():
    return "Weather info"

if __name__=="__main__":
    print("executing main block")
    app.run(port=3000)

