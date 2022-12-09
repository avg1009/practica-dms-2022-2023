from typing import List, Dict
from http import HTTPStatus
from flask import current_app
from dms2223backend.data.db.results import Respuesta
from dms2223backend.data.db.resultsets import Respuestas
from dms2223backend.service import respuestaservice

def get_respuestas() :
    with current_app.app_context() :
        respuestas: List[Respuesta] = respuestaservice.RespuestaService.list_respuestas()
        #incompleto
    return respuestas, HTTPStatus.OK.value


def post_respuesta(descripcion: str, qid: int):
    with current_app.app_context() :
        nuevaRespuesta : Respuesta = respuestaservice.RespuestaService.create_respuesta(descripcion, qid)
        if respuestaservice.RespuestaService.exists_respuesta(descripcion,qid):
            return nuevaRespuesta, HTTPStatus.CREATED.value
        else:
            return ('No se ha creado el argumento', HTTPStatus.NOT_FOUND.value)

def get_respuesta(descripcion : str, aid : int) :
    with current_app.app_context() :
        if (respuestaservice.RespuestaService.exists_respuesta(descripcion, aid)) :
            respuesta : Respuesta = respuestaservice.RespuestaService.get_respuesta(aid)
        else :
            return ('No se ha encontrado el argumento', HTTPStatus.NOT_FOUND.value)
        
    return respuesta, HTTPStatus.OK.value

def post_voto(aid: int):
    pass