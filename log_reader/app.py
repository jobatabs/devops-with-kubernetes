import os
from flask import Flask, send_file

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")
app.config["PORT"] = os.getenv("PORT")

@app.route("/")
def index():
    return send_file("/app/share/file.txt")
