## INPUT NAME ATTRIBUTE

from flask import Flask
app = Flask(__name__)
@app.route("/")
def home():
    return """
    <form>
      Name:
        <input name="Emp_Name">
      </form>
      """
app.run()