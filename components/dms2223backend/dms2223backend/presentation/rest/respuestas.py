from typing import List, Dict
from http import HTTPStatus
from flask import current_app
from dms2223backend.service import RespuestaService
from dms2223backend.service import PreguntaService
import dms2223common.data.Respuesta as common
#from dms2223backend.service import votoService

def get_respuestas(qid: int) :
    with current_app.app_context() :
        if PreguntaService.exits_pregunta(qid,current_app.db):
            return RespuestaService.list_respuestas(qid,current_app.db), HTTPStatus.OK.value
        else:
            return ("La pregunta no existe", HTTPStatus.NOT_FOUND.value)

def post_respuesta(respuesta: common.Respuesta, qid: int):
    with current_app.app_context() :
        try:
            return RespuestaService.create_respuesta_from_common(respuesta, qid ,current_app.db), HTTPStatus.CREATED.value
        except Exception:
            return ('No se ha creado el argumento', HTTPStatus.NOT_FOUND.value)

def get_respuesta(aid : int) :
    with current_app.app_context() :
        if (RespuestaService.exists_respuesta(aid,current_app.db)) :
            return RespuestaService.get_respuesta(aid,current_app.db),HTTPStatus.OK.value
        else :
            return ('No se ha encontrado el argumento', HTTPStatus.NOT_FOUND.value)

def post_voto(descripcion: str, aid: int):
    # with current_app.app_context() :
    #     try:
    #         if (votoService.exists_voto(aid)) : 
    #             return votoService.create_voto_respuesta(descripcion, aid), HTTPStatus.CREATED.value
    #         else :
    #             return ('Ya se ha votado esta respuesta', HTTPStatus.ALREADY_REPORTED.value)
    #     except Exception:
    #         return ('No se ha creado el argumento', HTTPStatus.NOT_FOUND.value)
    pass