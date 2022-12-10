from typing import List, Dict
from http import HTTPStatus
from flask import current_app
from dms2223backend.service import reporteservice
# from dms2223backend.service import preguntaservice
# from dms2223backend.service import respuestaservice
# from dms2223backend.service import comentarioservice

def post_reporte_pregunta(descripcion: str, qid: int):
# with current_app.app_context() :
# if preguntaservice.PreguntaService.exits_pregunta(qid):
# return reportesrvice.ReporteService.create_reporte(descripcion,qid), HTTPStatus.OK.value
# else:
# return ("La pregunta no existe", HTTPStatus.NOT_FOUND.value)
    pass
def get_reportes_preguntas():
# with current_app.app_context() :
# return reportesrvice.ReporteService.list_reportes_preguntas(current_app.db),HTTPStatus.OK.value
    pass
def set_status_pregunta(qrid: int):
    pass

def post_reporte_respuesta(descripcion: str,aid: int):
# with current_app.app_context() :
# if respuestaservice.RespuestaService.exits_respuesta(aid):
# return reportesrvice.ReporteService.create_reporte(descripcion,aid), HTTPStatus.OK.value
# else:
# return ("La respuesta no existe", HTTPStatus.NOT_FOUND.value)
    pass
def get_reportes_respuestas():
# with current_app.app_context() :
# return reportesrvice.ReporteService.list_reportes_respuestas(current_app.db),HTTPStatus.OK.value
    pass
def set_status_respuesta(arid: int):
    pass

def post_reporte_comentario(descripcion: str, cid: int):
# with current_app.app_context() :
# if comentarioservice.ComentarioService.exits_comentario(cid):
# return reportesrvice.ReporteService.create_reporte(descripcion,cid), HTTPStatus.OK.value
# else:
# return ("El comentario no existe", HTTPStatus.NOT_FOUND.value)
    pass

def get_reportes_comentarios():
# with current_app.app_context() :
# return reportesrvice.ReporteService.list_reportes_comentarios(current_app.db),HTTPStatus.OK.value
    pass
def set_status_comentario(crid: int):
    pass