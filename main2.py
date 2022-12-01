from flask import Flask, request, redirect
from replit import db
# imports request and redirect as well as flask

app = Flask(__name__, static_url_path='/static')
# path to the static file that stores my images

# users = {}
# users["david"] = {"password": "babe"}
# users["katie"] = {"password": "k8t"}
# A dictionary hard coded into the program that stores the login details for two users
# db["mikee"] = {"password": "owinoo"}
# db["katie"] = {"password": "k8t"}
# change the assignment of the next two lines to store the data in the database instead.


@app.route('/login', methods=["POST"])
def login():
    form = request.form
    try:
        if db[request.
              form["username"]]["password"] == request.form["password"]:
            return redirect("/yup")
        else:
            return redirect("/nope")
    except:
        return redirect("/nope")


# Login checking code - uses POST because it's dealing with usernames & passwords so we want encryption

# If the user details are correct, they get a lovely success gif, if not, they get a 'nope' gif.

# Try except used to load the 'nope' in case there's an error.


@app.route("/nope")
def nope():
    return """<img src="static/nerdy.gif" height="100">"""


@app.route("/yup")
def yup():
    page = """<img src="static/yup.gif" height="100">"""
    f = open("change.html", "r")
    page += f.read()
    f.close()
    return page


@app.route("/changePass", methods=["POST"])
def change():
    form = request.form

    db[request.form["username"]]["password"] = request.form["newPassword"]
    return f"""Password changed to {request.form['newPassword']}"""


# The two methods above load the relevant gif depending on the result of the '/login' method


@app.route('/')
def index():
    page = ""
    f = open("login.html", "r")
    page = f.read()
    f.close()
    return page


# Loads the login HTML page that I've built separately on run.

app.run(host='0.0.0.0', port=81)
