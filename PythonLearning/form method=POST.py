## form method="POST"

from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <form method="POST">

        Name:
        <input name="emp_name">

        <button>Add Employee</button>

    </form>
    """

app.run()