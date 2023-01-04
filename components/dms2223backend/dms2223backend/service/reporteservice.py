from datetime import datetime
from typing import List, Dict
from sqlalchemy.orm.session import Session
from dms2223backend.data.db.schema import Schema  # type: ignore
from dms2223backend.data.db.results.reportes import ReporteComentario
from dms2223backend.data.db.results.reportes import ReportePregunta
from dms2223backend.data.db.results.reportes import ReporteRespuesta
from dms2223common.data.reportstatus import ReportStatus
from dms2223backend.data.db.resultsets.reportes import ReporteComentarios
from dms2223backend.data.db.resultsets.reportes import ReporteRespuestas
from dms2223backend.data.db.resultsets.reportes import ReportePreguntas

from dms2223backend.data.db.results import Pregunta, Respuesta, Comentario
from dms2223backend.data.db.resultsets import Preguntas, Respuestas, Comentarios


from dms2223common.data.reportstatus import ReportStatus
import dms2223common.data.Pregunta as common
import dms2223common.data.Respuesta as common
import dms2223common.data.Comentario as common
import dms2223common.data.Reporte as common
from flask import current_app
#TODO
class ReporteService:

    @staticmethod
    def create_reporte_pregunta(descripcion: str, creador: str,pregunta: int, estado: ReportStatus, fecha:str ,schema: Schema) -> common.Reporte:
        session: Session = schema.new_session()
        out: common.Reporte = None
        try:
            elemento : Pregunta = Preguntas.get_pregunta(session, pregunta)
            new_reporte: ReportePregunta = ReportePreguntas.create(session,descripcion,creador, pregunta, estado,fecha)
            pregunta: common.Pregunta = common.Pregunta(elemento.creador,elemento.titulo,elemento.descripcion,elemento.id,datetime.fromisoformat(elemento.fechaCreacion))
            out = common.Reporte(new_reporte.descripcion, new_reporte.creador, pregunta, new_reporte.estado, new_reporte.id ,datetime.fromisoformat(new_reporte.fechaCreacion))
        except Exception as ex:
            raise ex
        finally:
            schema.remove_session()
        return out

    @staticmethod
    def create_reporte_pregunta_from_common(reporte: common.Reporte, schema: Schema) -> common.Reporte:
        return ReporteService.create_reporte_pregunta(reporte.getDescripcion(), reporte.getAutor(),reporte.getElemento().getId(),reporte.getEstado(),reporte.getFechaReporte().isoformat(), schema)
   
    @staticmethod
    def create_reporte_respuesta(descripcion: str, creador: str,respuesta: common.Respuesta, estado: ReportStatus,fecha:str,schema: Schema) -> common.Reporte:
        session: Session = schema.new_session()
        out: common.Reporte = None
        try:
            new_reporte: ReporteRespuesta = ReporteRespuestas.create(session,descripcion, creador, respuesta.getId(), estado,fecha)
            elemento : Respuesta = Respuestas.get_respuesta(session, new_reporte.id_respuesta)
            out = common.Reporte(new_reporte.descripcion, new_reporte.creador, elemento, new_reporte.estado, new_reporte.id,new_reporte.fechaReporte)
        except Exception as ex:
            raise ex
        finally:
            schema.remove_session()
        return out
    
    @staticmethod
    def create_reporte_respuesta_from_common(reporte: common.Reporte, respuesta: common.Respuesta, schema: Schema) -> common.Reporte:
        return ReporteService.create_reporte_respuesta(reporte.getDescripcion(), reporte.getAutor(),respuesta,reporte.getEstado(),reporte.getFechaReporte() ,schema)
    
    @staticmethod
    def create_reporte_comentario(descripcion: str, creador: str,comentario: common.Comentario, estado: ReportStatus,fecha:str,schema: Schema) -> common.Reporte:
        session: Session = schema.new_session()
        out: common.Reporte = None
        try:
            new_reporte: ReporteComentario = ReporteComentarios.create(session,descripcion, creador, comentario.getId(),estado,fecha)
            elemento : Comentario = Comentarios.get_comentario(session, new_reporte.id_comentario)
            out = common.Reporte(new_reporte.descripcion, new_reporte.creador, elemento, new_reporte.estado, new_reporte.id,new_reporte.fechaReporte)
        except Exception as ex:
            raise ex
        finally:
            schema.remove_session()
        return out
        
    @staticmethod
    def create_reporte_comentario_from_common(reporte: common.Reporte, comentario: common.Comentario, schema: Schema) -> common.Reporte:
        return ReporteService.create_reporte_comentario(reporte.getDescripcion(), reporte.getAutor(),comentario,reporte.getEstado(),reporte.getFechaReporte(), schema)

    @staticmethod
    def exists_reporte_pregunta(id:int,schema: Schema):
        session: Session = schema.new_session()
        reporte_exists: bool = ReportePreguntas.get_reporte(session,id)
        schema.remove_session()
        return reporte_exists

    @staticmethod
    def exists_reporte_respuesta(id:int,schema: Schema):
        session: Session = schema.new_session()
        reporte_exists: bool = ReporteRespuestas.get_reporte(session,id)
        schema.remove_session()
        return reporte_exists

    @staticmethod
    def exists_reporte_comentario(id:int, schema: Schema):
        session: Session = schema.new_session()
        reporte_exists: bool = ReporteComentarios.get_reporte(session,id)
        schema.remove_session()
        return reporte_exists


    @staticmethod
    def list_reportes(schema: Schema) -> List[common.Reporte]:
        out: List[common.Reporte] = []
        session: Session = schema.new_session()
        reportes: List[ReportePregunta] = ReportePreguntas.list_all(session)
        for reporte in reportes:
            elemento : Pregunta = Preguntas.get_pregunta(session, reporte.id_pregunta)
            pregunta: common.Pregunta = common.Pregunta(elemento.creador,elemento.titulo,elemento.descripcion,elemento.id,datetime.fromisoformat(elemento.fechaCreacion))
            out.append(common.Reporte(reporte.descripcion,reporte.creador, pregunta,reporte.estado,reporte.id,datetime.fromisoformat(reporte.fechaCreacion)))
        reportes: List[ReporteRespuesta] = ReporteRespuestas.list_all(session)
        for reporte in reportes:
            elemento : Respuesta = Respuestas.get_respuesta(session, reporte.id_respuesta)
            out.append(common.Reporte(reporte.descripcion,reporte.creador, elemento,reporte.estado,reporte.id,datetime.fromisoformat(reporte.fechaCreacion)))
        reportes: List[ReporteComentario] = ReporteComentarios.list_all(session)
        for reporte in reportes:
            elemento : Comentario = Comentarios.get_comentario(session, reporte.id_comentario)
            out.append(common.Reporte(reporte.descripcion,reporte.creador, elemento,reporte.estado,reporte.id,datetime.fromisoformat(reporte.fechaCreacion)))
        schema.remove_session()
        return out

    @staticmethod
    def get_reporte_pregunta(id : int, schema: Schema) -> common.Reporte:
        session : Session = schema.new_session()
        reporte_pregunta : ReportePregunta = ReportePreguntas.get_reporte(session, id)
        elemento : Pregunta = Preguntas.get_pregunta(session, reporte_pregunta.id_pregunta)
        out: common.Reporte = common.Reporte(reporte_pregunta.descripcion, reporte_pregunta.creador, elemento, reporte_pregunta.estado, reporte_pregunta.id,reporte_pregunta.fechaCreacion)
        schema.remove_session()
        return out
    
    @staticmethod
    def get_reporte_respuesta(id : int, schema: Schema) -> common.Reporte:
        session : Session = schema.new_session()
        reporte_respuesta : ReporteRespuesta = ReporteRespuestas.get_reporte(session, id)
        elemento : Respuesta = Respuestas.get_respuesta(session, reporte_respuesta.id_respuesta)
        out: common.Reporte = common.Reporte(reporte_respuesta.descripcion, reporte_respuesta.creador, elemento, reporte_respuesta.estado, reporte_respuesta.id,reporte_respuesta.fechaReporte)
        schema.remove_session()
        return out
    
    @staticmethod
    def get_reporte_comentario(id : int, schema: Schema) -> common.Reporte:
        session : Session = schema.new_session()
        reporte_comentario : ReporteComentario = ReporteComentarios.get_reporte(session, id)
        elemento : Comentario = Comentarios.get_comentario(session, reporte_comentario.id_comentario)
        out: common.Reporte = common.Reporte(reporte_comentario.descripcion, reporte_comentario.creador, elemento, reporte_comentario.estado, reporte_comentario.id,reporte_comentario.fechaReporte)
        schema.remove_session()
        return out