from typing import List, Dict
from http import HTTPStatus
from flask import current_app
from dms2223backend.service import respuestaservice
from dms2223backend.service import preguntaservice
#from dms2223backend.service import votosService

def get_respuestas(qid: int) :
    with current_app.app_context() :
        if preguntaservice.PreguntaService.exits_pregunta(qid):
            return respuestaservice.RespuestaService.list_respuestas(qid), HTTPStatus.OK.value
        else:
            return ("La pregunta no existe", HTTPStatus.NOT_FOUND.value)

def post_respuesta(descripcion: str, qid: int):
    with current_app.app_context() :
        try:
            return respuestaservice.RespuestaService.create_respuesta(descripcion, qid), HTTPStatus.CREATED.value
        except Exception:
            return ('No se ha creado el argumento', HTTPStatus.NOT_FOUND.value)

def get_respuesta(descripcion : str, aid : int) :
    with current_app.app_context() :
        if (respuestaservice.RespuestaService.exists_respuesta(aid)) :
            return respuestaservice.RespuestaService.get_respuesta(aid),HTTPStatus.OK.value
        else :
            return ('No se ha encontrado el argumento', HTTPStatus.NOT_FOUND.value)

def post_voto(descripcion: str, aid: int):
    # with current_app.app_context() :
    #     try:
    #         if (votosService.votoService.exists_voto(aid)) : 
    #             return votosService.votoService.create_voto_respuesta(descripcion, aid), HTTPStatus.CREATED.value
    #         else :
    #             return ('Ya se ha votado esta respuesta', HTTPStatus.ALREADY_REPORTED.value)
    #     except Exception:
    #         return ('No se ha creado el argumento', HTTPStatus.NOT_FOUND.value)
    pass