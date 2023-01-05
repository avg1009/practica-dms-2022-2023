import traceback
from typing import List, Dict
from http import HTTPStatus
from flask import current_app
from dms2223backend.service.comentarioservice import ComentarioService
from dms2223backend.service import RespuestaService
from dms2223backend.service import PreguntaService
from dms2223common.data.Respuesta import Respuesta
#from dms2223backend.service import VotoService

def get_respuestas(qid: int) :
    with current_app.app_context() :
        if PreguntaService.exists_pregunta(qid,current_app.db):
            pregunta = PreguntaService.get_pregunta(qid,current_app.db)
            respuestas = RespuestaService.list_respuestas(qid,current_app.db)
            
            for respuesta in respuestas:
                comentarios = ComentarioService.list_comentarios(respuesta.getId(),current_app.db)
                for comentario in comentarios:
                    respuesta.addComentario(comentario)
                pregunta.addRespuesta(respuesta)
                
            return pregunta.to_json(), HTTPStatus.OK.value
        else:
            return ("La pregunta no existe", HTTPStatus.NOT_FOUND.value)

def post_respuesta(body: dict, qid: int):
    with current_app.app_context() :
        try:
            respuesta = Respuesta.from_json(body,True)
            return RespuestaService.create_respuesta_from_common(respuesta, qid ,current_app.db).to_json(), HTTPStatus.CREATED.value
        except Exception as e:
            current_app.logger.error(traceback.format_exception(e))
            return (str(e), HTTPStatus.NOT_FOUND.value)

def get_respuesta(aid : int) :
    with current_app.app_context() :
        if (RespuestaService.exists_respuesta(aid,current_app.db)) :
            return RespuestaService.get_respuesta(aid,current_app.db).to_json(),HTTPStatus.OK.value
        else :
            return ('No se ha encontrado el argumento', HTTPStatus.NOT_FOUND.value)

def post_voto( aid: int):
    with current_app.app_context() :
        try:
            #if (VotoService.exists_voto_respuesta(aid)) : 
            #    return VotoService.create_voto_respuesta(aid), HTTPStatus.CREATED.value
            #else :
                return ('Ya se ha votado esta respuesta', HTTPStatus.ALREADY_REPORTED.value)
        except Exception:
            return ('No se ha creado el argumento', HTTPStatus.NOT_FOUND.value)
    pass