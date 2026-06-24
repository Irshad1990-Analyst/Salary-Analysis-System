## How to add employee name
## methods=["GET", "POST"]
## if request.method == "POST":
##  name = request.form["emp_name"]
## return "Hello " + name


from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    if request.method == "POST":

        name = request.form["emp_name"]

        return "Hello " + name

    return """
    <form method="POST">

        Name:
        <input name="emp_name">

        <button>Submit</button>

    </form>
    """

app.run()