from typing import List, Dict
from http import HTTPStatus
from flask import current_app
from dms2223backend.service import preguntaservice

def get_preguntas() :
    with current_app.app_context() :
        return preguntaservice.PreguntaService.list_preguntas(current_app.db),HTTPStatus.OK.value

def post_pregunta(titulo: str, descripcion: str):
    with current_app.app_context() :

        try:
            return preguntaservice.PreguntaService.create_pregunta(titulo, descripcion), HTTPStatus.CREATED.value
        except Exception:
            return ('No se ha creado el argumento', HTTPStatus.NOT_FOUND.value)

def get_pregunta(qid: int):
    with current_app.app_context() :

        if (preguntaservice.PreguntaService.exists_preguna(qid)) :
            return preguntaservice.PreguntaService.get_pregunta(qid), HTTPStatus.NOT_FOUND.value
        else:
            return ('No se ha encontrado el argumento', HTTPStatus.NOT_FOUND.value)

