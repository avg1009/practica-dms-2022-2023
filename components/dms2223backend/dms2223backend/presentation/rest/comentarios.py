from typing import List, Dict
from http import HTTPStatus
from flask import current_app
from dms2223backend.service import ComentarioService
from dms2223backend.service import RespuestaService
#from dms2223backend.service import votoService

def get_comentarios(aid) :
    with current_app.app_context() :
        if RespuestaService.exits_respuesta(aid):
            return ComentarioService.list_comentarios(aid), HTTPStatus.OK.value
        else:
            return ("La respuesta no existe", HTTPStatus.NOT_FOUND.value)

def post_comentario_respuesta(descripcion: str, qid: int):
    with current_app.app_context() :
        try:
            return ComentarioService.create_comentario(descripcion, qid), HTTPStatus.CREATED.value
        except Exception:
            return ('No se ha creado el argumento', HTTPStatus.NOT_FOUND.value)

def get_comentarios(descripcion : str, cid : int) :
    with current_app.app_context() :
        if (ComentarioService.exists_comentario(descripcion, cid)) :
            return ComentarioService.get_comentario(cid), HTTPStatus.OK.value
        else :
            return ('No se ha encontrado el argumento', HTTPStatus.NOT_FOUND.value)

def post_voto(descripcion: str, cid: int):
    # with current_app.app_context() :
    #     try:
    #         if (votoService.exists_voto(cid)) : 
    #             return votoService.create_voto_comentario(descripcion, cid), HTTPStatus.CREATED.value
    #         else :
    #             return ('Ya se ha votado este comentario', HTTPStatus.ALREADY_REPORTED.value)
    #     except Exception:
    #         return ('No se ha creado el argumento', HTTPStatus.NOT_FOUND.value)
    pass
