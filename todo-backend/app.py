import json
from os import getenv
from flask import Flask, make_response, redirect, request

app = Flask(__name__)
app.secret_key = getenv("SECRET_KEY")
app.config["PORT"] = getenv("PORT")

todos = []

@app.route("/todos", methods=["GET"])
def todos_get():
    response = make_response(json.dumps(todos), 200)
    response.mimetype = "application/json"
    return response

@app.route("/todos", methods=["POST"])
def todos_post():
    todos.append(request.form["todo"])
    return redirect("/", 301)
