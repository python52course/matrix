import re

from requests import Response, get
from requests.exceptions import ConnectTimeout, ReadTimeout

from app.exceptions import HTTPException


def get_byte_matrix(url: str) -> bytes:
    try:
        response: Response = get(url, timeout=5)
    except (ConnectTimeout, ReadTimeout):
        raise ConnectTimeout("Couldn't get a response from to the remote server, try it later")
    if not response.ok:
        raise HTTPException(f"The server responded with an error for url: {url}")
    return response.content


def create_matrix_from_bytes(row_matrix: str) -> list[list[int]]:
    rows = (line for line in row_matrix.split("\n") if line.startswith("|"))
    matrix = []
    for row in rows:
        matrix.append(list(map(int, re.findall(r"\d+", row))))
    return matrix
