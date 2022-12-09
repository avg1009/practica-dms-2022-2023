from typing import List, Dict
from http import HTTPStatus
from flask import current_app
from dms2223backend.data.db.results import Pregunta
from dms2223backend.data.db.resultsets import Preguntas
from dms2223backend.service import preguntaservice

def get_preguntas() :
    with current_app.app_context() :
        preguntas: List[Pregunta] = preguntaservice.PreguntaService.list_preguntas(current_app.db)

    return preguntas, HTTPStatus.OK.value

def post_pregunta(titulo: str, descripcion: str):
    with current_app.app_context() :
        nuevaPregunta : Pregunta = preguntaservice.PreguntaService.create_pregunta(titulo, descripcion)
    return nuevaPregunta, HTTPStatus.CREATED.value

def get_pregunta(qid: int):
    with current_app.app_context() :
        if (preguntaservice.PreguntaService.exists_preguna(qid)) :
            pregunta : Pregunta = preguntaservice.PreguntaService.get_pregunta(qid)
        else :
            return ('No se ha encontrado el argumento', HTTPStatus.NOT_FOUND.value)
        
    return pregunta, HTTPStatus.OK.value
