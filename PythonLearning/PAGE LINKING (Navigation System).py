from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Home Page</h1>
    <a href="/employee">Go to Employee Page</a>
    """

@app.route("/employee")
def employee():
    return "<h1>Employee Page</h1>"

app.run()