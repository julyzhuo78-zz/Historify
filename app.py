from flask import Flask
from flask import render_template
from datetime import datetime
app = Flask(__name__)

@app.route("/")
def home(name = None):
    return render_template(
        "homepage.html",
        name = name,
        date = datetime.now()
    )
