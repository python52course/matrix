SOURCE_URL = (
    "https://raw.githubusercontent.com/avito-tech/python-trainee-assignment/main/matrix.txt"
)


MATRIX = [
    [10, 20, 30, 40],
    [50, 60, 70, 80],
    [90, 100, 110, 120],
    [130, 140, 150, 160],
]


def read_matrix_from_file() -> str:
    with open("app/tests/matrix.txt") as f:
        return f.read()
