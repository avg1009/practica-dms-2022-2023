from typing import List, Dict
from http import HTTPStatus
from flask import current_app
from dms2223backend.service import comentarioservice

def get_comentarios() :
    with current_app.app_context() :
        comentarios: List[Dict] = comentarioservice.ComentarioService.list_comentarios()

    return comentarios, HTTPStatus.OK.value

def post_comentario(descripcion: str, qid: int):
    with current_app.app_context() :
        nuevoComentario : Dict = comentarioservice.ComentarioService.create_comentario(descripcion, qid)
    return nuevoComentario, HTTPStatus.OK.value

def get_comentarios(descripcion : str, cid : int) :
    with current_app.app_context() :
        if (comentarioservice.ComentarioService.exists_comentario(descripcion, cid)) :
            comentario : Dict = comentarioservice.ComentarioService.get_comentario(cid)
        else :
            return ('No se ha encontrado el argumento', HTTPStatus.BAD_REQUEST.value)
        
    return comentario, HTTPStatus.OK.value

def post_voto(cid: int):
    pass
