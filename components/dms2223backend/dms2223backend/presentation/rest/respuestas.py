from typing import List, Dict
from http import HTTPStatus
from flask import current_app
from dms2223backend.service import respuestaservice

def get_respuestas() :
    with current_app.app_context() :
        respuestas: List[Dict] = respuestaservice.RespuestaService.list_respuestas()

    return respuestas, HTTPStatus.OK.value


def post_respuesta(descripcion: str, qid: int):
    with current_app.app_context() :
        nuevaRespuesta : Dict = respuestaservice.RespuestaService.create_respuesta(descripcion, qid)
    return nuevaRespuesta, HTTPStatus.OK.value

def get_respuesta(descripcion : str, aid : int) :
    with current_app.app_context() :
        if (respuestaservice.RespuestaService.exists_respuesta(descripcion, aid)) :
            respuesta : Dict = respuestaservice.RespuestaService.get_respuesta(aid)
        else :
            return ('No se ha encontrado el argumento', HTTPStatus.BAD_REQUEST.value)
        
    return respuesta, HTTPStatus.OK.value

def post_voto(aid: int):
    pass