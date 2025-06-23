import logging
from os import getenv
from flask import Flask
from dotenv import load_dotenv

load_dotenv()

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

app = Flask(__name__)
app.secret_key = getenv("SECRET_KEY")
app.config["PORT"] = getenv("PORT")

test_env = getenv("TEST_ENV") == "true"
app.logger.info(f"Test environment: {test_env}")
app.logger.info(f"Server running on port {app.config['PORT']}")
#if __name__ == "__main__":
  #  app.run(port=app.config["PORT"], host="0.0.0.0", debug=test_env)
