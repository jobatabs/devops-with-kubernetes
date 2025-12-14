import json
import logging
from os import getenv
from flask import Flask, make_response, redirect, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

app = Flask(__name__)
app.secret_key = getenv("SECRET_KEY")
app.config["PORT"] = getenv("PORT")
app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URL")

db = SQLAlchemy(app)

app.logger.info("Running")
app.logger.info("Server running on port %s", app.config['PORT'])

@app.route("/todos", methods=["GET"])
def todos_get():
    app.logger.info("GET request received")
    result = db.session.execute(text("SELECT name FROM todos;")).fetchall()
    todos = []
    for todo in result:
        todos.append(todo[0])
    response = make_response(json.dumps(todos), 200)
    response.mimetype = "application/json"
    app.logger.info("GET request handled")
    return response

@app.route("/todos", methods=["POST"])
def todos_post():
    name = request.form["todo"]
    if len(name) > 140:
        app.logger.info("Entry too long, not accepted: %s...", name[0:140])
        return redirect("/", 400)
    app.logger.info("POST request received: %s", name)
    sql = text("INSERT INTO todos (name) VALUES (:name) RETURNING name;")
    app.logger.info("SQL statement formed: %s", str(sql))
    result = db.session.execute(sql, {"name": name})
    db.session.commit()
    app.logger.info("SQL statement handled: %s", result.scalar())
    app.logger.info("POST request handled")
    return redirect("/", 301)
