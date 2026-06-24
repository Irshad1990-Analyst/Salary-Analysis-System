## FLASK CLASS 4 HTML INTRODUCTION

from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Home Page</h1>
    <p>Welcome Irshad</p>
    """

app.run()
