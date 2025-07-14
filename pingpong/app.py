from os import getenv
from flask import Flask, make_response

app = Flask(__name__)
app.secret_key = getenv("SECRET_KEY")
app.config["PORT"] = getenv("PORT")
app.config["PONG"] = 0

@app.route("/pingpong")
def pong():
    response = make_response(make_pong(), 200)
    response.mimetype = "text/plain"
    return response

def make_pong():
    answer = f"pong {app.config['PONG']}"
    app.config["PONG"] += 1
    return answer
