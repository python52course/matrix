from flask.testing import FlaskClient


def test_connection(client: FlaskClient) -> None:
    response = client.get("/ping")

    assert response.status_code == 200
    assert response.json == {"ping": "pong"}
