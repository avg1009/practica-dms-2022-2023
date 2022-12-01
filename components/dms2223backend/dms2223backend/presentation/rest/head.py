from http import HTTPStatus

def get() -> tuple[str, HTTPStatus]:
    return '', HTTPStatus.NOT_FOUND