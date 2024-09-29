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
