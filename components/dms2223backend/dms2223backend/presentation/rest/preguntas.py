from typing import List, Dict
from http import HTTPStatus
from flask import current_app
from dms2223backend.service import PreguntaService
import dms2223common.data.Pregunta as common

def get_preguntas() :
    with current_app.app_context() :
        preguntas: List(common.Pregunta) = PreguntaService.list_preguntas(current_app.db)
        salida = []
        for pregunta in preguntas:
            salida.append(pregunta.to_json())
            
        return salida, HTTPStatus.OK.value

def post_pregunta(pregunta: common.Pregunta):
    with current_app.app_context() :

        try:
            return PreguntaService.create_pregunta_from_common(pregunta, current_app.db), HTTPStatus.CREATED.value
        except Exception:
            return ('No se ha creado el argumento', HTTPStatus.NOT_FOUND.value)

def get_pregunta(qid: int):
    with current_app.app_context() :

        if (PreguntaService.exists_pregunta(qid,current_app.db)) :
            return PreguntaService.get_pregunta(qid,current_app.db), HTTPStatus.NOT_FOUND.value
        else:
            return ('No se ha encontrado el argumento', HTTPStatus.NOT_FOUND.value)

