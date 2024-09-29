from app.helpers import MATRIX, read_matrix_from_file
from app.utils import create_matrix_from_bytes


def test_create_matrix_by_bytes():
    assert create_matrix_from_bytes(read_matrix_from_file()) == MATRIX
