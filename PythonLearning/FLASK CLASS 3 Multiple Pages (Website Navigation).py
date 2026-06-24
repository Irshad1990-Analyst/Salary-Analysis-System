## FLASK CLASS 3 Multiple Pages (Website Navigation)

from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Home Page"

@app.route("/employee")
def employee():
    return "Employee Page"

@app.route("/add")
def add():
    return "Add Employee Page"

app.run()