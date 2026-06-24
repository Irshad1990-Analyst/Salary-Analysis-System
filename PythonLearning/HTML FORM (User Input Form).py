from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Add Employee</h1>

    <form>
        Name:
        <input>

        <button>Add Employee</button>
    </form>
    """

app.run()