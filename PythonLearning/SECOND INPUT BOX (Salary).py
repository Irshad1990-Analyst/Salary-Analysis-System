from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    if request.method == "POST":

        name = request.form["emp_name"]

        salary = request.form["salary"]

        return name + " " + salary

    return """
    <form method="POST">

        Name:
        <input name="emp_name">

        <br><br>

        Salary:
        <input name="salary">

        <br><br>

        <button>Submit</button>

    </form>
    """

app.run()