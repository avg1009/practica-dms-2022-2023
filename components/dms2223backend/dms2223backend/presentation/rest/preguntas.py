from typing import List, Dict
from http import HTTPStatus
from flask import current_app
from dms2223backend.service import PreguntaService

def get_preguntas() :
    with current_app.app_context() :
        return PreguntaService.list_preguntas(current_app.db),HTTPStatus.OK.value

def post_pregunta(titulo: str, descripcion: str):
    with current_app.app_context() :

        try:
            return PreguntaService.create_pregunta(titulo, descripcion), HTTPStatus.CREATED.value
        except Exception:
            return ('No se ha creado el argumento', HTTPStatus.NOT_FOUND.value)

def get_pregunta(qid: int):
    with current_app.app_context() :

        if (PreguntaService.exists_pregunta(qid)) :
            return PreguntaService.get_pregunta(qid), HTTPStatus.NOT_FOUND.value
        else:
            return ('No se ha encontrado el argumento', HTTPStatus.NOT_FOUND.value)

