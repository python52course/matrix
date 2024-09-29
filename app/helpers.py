SOURCE_URL = (
    "https://raw.githubusercontent.com/avito-tech/python-trainee-assignment/main/matrix.txt"
)


def read_matrix_from_file() -> str:
    with open("app/tests/matrix.txt") as f:
        return f.read()
