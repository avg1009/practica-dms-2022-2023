import traceback
from typing import List, Dict
from http import HTTPStatus
from flask import current_app
from dms2223backend.service import ComentarioService
from dms2223backend.service import RespuestaService
from dms2223common.data.Comentario import Comentario
#from dms2223backend.service import VotoService

def get_comentarios(aid) :
    with current_app.app_context() :
        if RespuestaService.exits_respuesta(aid,current_app.db):
            return ComentarioService.list_comentarios(aid,current_app.db), HTTPStatus.OK.value
        else:
            return ("La respuesta no existe", HTTPStatus.NOT_FOUND.value)

def post_comentario_respuesta(body: dict, aid: int):
    with current_app.app_context() :
        try:
            comentario = Comentario.from_json(body,True)
            return ComentarioService.create_comentario_from_common(comentario, aid, current_app.db).to_json(), HTTPStatus.CREATED.value
        except Exception as e:
            current_app.logger.error(traceback.format_exception(e))
            return (str(e), HTTPStatus.NOT_FOUND.value)

def get_comentario(cid : int) :
    with current_app.app_context() :
        if (ComentarioService.exists_comentario(cid,current_app.db)) :
            return ComentarioService.get_comentario(cid,current_app.db).to_json(), HTTPStatus.OK.value
        else :
            return ('No se ha encontrado el argumento', HTTPStatus.NOT_FOUND.value)

def post_voto(descripcion: str, cid: int):
    with current_app.app_context() :
        try:
            #if (VotoService.exists_voto_comentario(cid)) : 
            #    return VotoService.create_voto_comentario(descripcion, cid), HTTPStatus.CREATED.value
            #else :
                return ('Ya se ha votado este comentario', HTTPStatus.ALREADY_REPORTED.value)
        except Exception:
            return ('No se ha creado el argumento', HTTPStatus.NOT_FOUND.value)
    pass
