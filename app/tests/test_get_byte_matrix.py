import pytest
from requests import ConnectTimeout

from app.exceptions import HTTPException
from app.helpers import SOURCE_URL, read_matrix_from_file
from app.utils import get_byte_matrix


def test_get_byte_matrix() -> None:
    matrix = read_matrix_from_file()
    assert get_byte_matrix(SOURCE_URL) == matrix.encode("utf-8")


def test_get_byte_matrix_http_exception() -> None:
    with pytest.raises(
        HTTPException, match=f"The server responded with an error for url: {SOURCE_URL + '404'}"
    ):
        get_byte_matrix(SOURCE_URL + "404")


def test_get_byte_matrix_connect_timeout() -> None:
    with pytest.raises(
        ConnectTimeout, match="Couldn't get a response from to the remote server, try it later"
    ):
        get_byte_matrix("https://example.com:21")
