from typing import List, Dict
from http import HTTPStatus
from flask import current_app
from dms2223backend.service.reporteservice import ReporteService
from dms2223backend.service.preguntaservice import PreguntaService
from dms2223backend.service.respuestaservice import RespuestaService
from dms2223backend.service.comentarioservice import ComentarioService
from dms2223common.data.Respuesta import Respuesta
from dms2223common.data.Pregunta import Pregunta
from dms2223common.data.Comentario import Comentario
from dms2223common.data.Reporte import Reporte
from dms2223common.data.reportstatus import ReportStatus
#TODO
def post_reporte_pregunta(body: dict,qid:int):
    with current_app.app_context() :
        if PreguntaService.exists_pregunta(qid,current_app.db):
            pregunta=PreguntaService.get_pregunta(qid,current_app.db)
            return ReporteService.create_reporte_pregunta_from_common(
                Reporte.from_json(body,pregunta,True), current_app.db).to_json(), HTTPStatus.OK.value
        else:
            return ("La pregunta no existe", HTTPStatus.NOT_FOUND.value)

def get_reportes():
    with current_app.app_context() :
        current_app.logger.debug(ReporteService.list_reportes(current_app.db))
        reportes = ReporteService.list_reportes(current_app.db)
        salida = []
        for reporte in reportes:
            salida.append(reporte.to_json())
        return salida,HTTPStatus.OK.value
    

def set_status_pregunta(rid: int, estado: ReportStatus):
    with current_app.app_context() :
        if ReporteService.exist_reporte_pregunta(rid,current_app.db):
            return ReporteService.update_reporte_pregunta_from_common(
                rid, estado, current_app.db), HTTPStatus.NO_CONTENT.value
        else:
            return ("La pregunta no existe", HTTPStatus.NOT_FOUND.value)
    

def post_reporte_respuesta(body: dict, aid: int):
    with current_app.app_context() :
        if RespuestaService.exists_respuesta(aid,current_app.db):
            respuesta = RespuestaService.get_respuesta(aid,current_app.db)
            return ReporteService.create_reporte_respuesta_from_common(
                Reporte.from_json(body,respuesta,True), current_app.db).to_json(), HTTPStatus.OK.value
        else:
            return ("La pregunta no existe", HTTPStatus.NOT_FOUND.value)

def set_status_respuesta(rid: int,estado: ReportStatus):
    with current_app.app_context() :
        if ReporteService.exist_reporte_respuesta(rid,current_app.db):
            return ReporteService.update_reporte_respuesta_from_common(
                rid, estado, current_app.db), HTTPStatus.NO_CONTENT.value
        else:
            return ("La pregunta no existe", HTTPStatus.NOT_FOUND.value)
    

def post_reporte_comentario(body: dict, cid: int):
    with current_app.app_context() :
        if ComentarioService.exists_comentario(cid,current_app.db):
            comentario = ComentarioService.get_comentario(cid,current_app.db)
            return ReporteService.create_reporte_comentario_from_common(
                Reporte.from_json(body,comentario,True), current_app.db).to_json(), HTTPStatus.OK.value
        else:
            return ("La pregunta no existe", HTTPStatus.NOT_FOUND.value)
 
def set_status_comentario(rid: int,estado: ReportStatus):
    with current_app.app_context() :
        if ReporteService.exist_reporte_comentario(rid,current_app.db):
            return ReporteService.update_reporte_comentario_from_common(
                rid, estado, current_app.db), HTTPStatus.NO_CONTENT.value
        else:
            return ("La pregunta no existe", HTTPStatus.NOT_FOUND.value)