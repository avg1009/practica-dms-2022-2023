import json
import time
from typing import Dict, Tuple, Optional
from http import HTTPStatus
from flask import current_app
from authlib.jose import JsonWebSignature  # type: ignore
from dms2223backend.data.config.backendconfiguration import BackendConfiguration


def health_test() -> Tuple[None, Optional[int]]:
    """Simple health test endpoint.

    Returns:
        - Tuple[None, Optional[int]]: A tuple of no content and code 204 No Content.
    """
    return (None, HTTPStatus.NO_CONTENT.value)