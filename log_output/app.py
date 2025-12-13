import uuid
import requests
from datetime import datetime, timezone
from os import getenv
from flask import Flask, render_template

app = Flask(__name__)
app.secret_key = getenv("SECRET_KEY")
app.config["PORT"] = getenv("PORT")
app.config["UUID"] = str(uuid.uuid4())
app.config["MESSAGE"] = getenv("MESSAGE")

@app.route("/")
def index():
    now = datetime.now(timezone.utc)
    now = now.strftime('%Y-%m-%dT%H:%M:%S.%fZ: ' + app.config["UUID"])
    ping = requests.get("http://pingpong-backend-svc:3000/pings").content.decode()
    print(now)
    with open("/config/information.txt", encoding="UTF-8") as f:
        file = f.readline()
    return render_template("index.html", output=now, pongs=ping, \
                           env=f"MESSAGE={app.config["MESSAGE"]}", file=file)
