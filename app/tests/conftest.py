from collections.abc import Generator

import pytest
from flask.testing import FlaskClient

from app.main import app


@pytest.fixture
def client() -> Generator[FlaskClient, None, None]:
    """
    A pytest fixture to create a test client for the Flask application.

    Returns:
        Generator[FlaskClient, None, None]: A generator that yields the test client.
    """
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client
