from os import getenv
from flask import Flask, make_response
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text

app = Flask(__name__)
app.secret_key = getenv("SECRET_KEY")
app.config["PORT"] = getenv("PORT")
app.config["SQLALCHEMY_DATABASE_URI"] = getenv("POSTGRES_URL")

db = SQLAlchemy(app)

with app.app_context():
    result = db.session.execute(text("SELECT count FROM pings WHERE id = 1;"))
    result = result.scalar()
    if result is not None:
        app.config["PONG"] = int(result)

@app.route("/pingpong")
def pong():
    response = make_response(make_pong(), 200)
    response.mimetype = "text/plain"
    return response

@app.route("/pings")
def pings():
    response = make_response(str(app.config["PONG"]), 200)
    response.mimetype = "text/plain"
    return response

def make_pong():
    answer = f"pong {app.config['PONG']}"
    sql = text("UPDATE pings SET count = count + 1")
    db.session.execute(sql)
    app.config["PONG"] += 1
    return answer
