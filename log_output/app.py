import uuid
from datetime import datetime, timezone
from os import getenv
from flask import Flask, render_template

app = Flask(__name__)
app.secret_key = getenv("SECRET_KEY")
app.config["PORT"] = getenv("PORT")
app.config["UUID"] = str(uuid.uuid4())

@app.route("/")
def index():
    now = datetime.now(timezone.utc)
    now = now.strftime('%Y-%m-%dT%H:%M:%S.%fZ: ' + app.config["UUID"])
    print(now)
    return render_template("index.html", output=now)
