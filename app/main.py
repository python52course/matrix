from flask import Flask

app = Flask(__name__)


@app.route("/ping")
def ping() -> dict:
    """
    A simple endpoint to check if the application is running.

    Returns:
        dict: A dictionary with the key "ping" and the value "pong".
    """
    return {"ping": "pong"}


def get_matrix(): ...
