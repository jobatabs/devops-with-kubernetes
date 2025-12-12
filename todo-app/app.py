import logging
from datetime import datetime, timedelta
from os import getenv
import requests
from flask import Flask, render_template
from dotenv import load_dotenv
from util import safe_open_w

load_dotenv()

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

app = Flask(__name__)
app.secret_key = getenv("SECRET_KEY")
app.config["PORT"] = getenv("PORT")
app.config["IMGPATH"] = "static/img.jpg"
app.config["IMGTIME"] = datetime.now()
with safe_open_w(app.config["IMGPATH"]) as file:
    r = requests.get("https://picsum.photos/1200", timeout=10)
    file.write(r.content)

test_env = getenv("TEST_ENV") == "true"
app.logger.info("Test environment: %s", test_env)
app.logger.info("Server running on port %s", app.config['PORT'])

@app.route("/")
def index():
    delta = datetime.now() - app.config["IMGTIME"]
    if delta > timedelta(seconds=10):
        with safe_open_w(app.config["IMGPATH"]) as f:
            new_file = requests.get("https://picsum.photos/1200", timeout=10)
            f.write(new_file.content)
        app.config["IMGTIME"] = datetime.now()
    todos = requests.get("http://todo-backend-svc:3000/todos").json()
    return render_template("index.html", todos=todos, image=app.config["IMGPATH"])
