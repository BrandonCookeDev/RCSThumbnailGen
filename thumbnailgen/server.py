import dotenv
from flask import Flask


app = Flask(__name__)


@app.route("/")
def hello():
    return 200


if __name__ == "__main__":
    app.run()
