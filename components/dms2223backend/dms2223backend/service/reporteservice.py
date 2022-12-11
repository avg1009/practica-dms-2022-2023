# from typing import List, Dict
# from sqlalchemy.orm.session import Session
# from dms2223backend.data.db.schema import Schema  # type: ignore
# from dms2223backend.data.db.results.reportes import ReporteComentario
# from dms2223backend.data.db.results.reportes import ReportePreguntas
# from dms2223backend.data.db.results.reportes import ReporteRespuesta
# from dms2223backend.data.db.resultsets import Preguntas
# from dms2223backend.data.db.resultsets.reportes import ReportesComentarios
# from dms2223backend.data.db.resultsets.reportes import ReportesRespuestas
# from dms2223backend.data.db.resultsets.reportes import ReportesPreguntas


# from dms2223common.data import reportstatus
# import dms2223common.data.Pregunta as common
# import dms2223common.data.Reporte as common
# #TODO
# class ReporteService:

#     @staticmethod
#     def create_reporte_pregunta(descripcion: str, creador: str,pregunta: common.Pregunta, estado: reportstatus,schema: Schema) -> common.Reporte:
#         session: Session = Schema.new_session()
#         out: common.Reporte = None
#         try:
#             new_reporte: ReportePreguntas = ReportesPreguntas.create(session,descripcion, pregunta,creador, estado)
#             out = common.Reporte(new_reporte.descripcion,
#             new_reporte.creador,
#             new_reporte.elemento,new_reporte.estado, new_reporte.id)
#         except Exception as ex:
#             raise ex
#         finally:
#             Schema.remove_session()
#         return out

#     @staticmethod
#     def create_reporte_respuesta_from_common(reporte: common.Reporte, respuesta: common.Respuesta, schema: Schema) -> common.Reporte:
#         return ReporteService.create_reporte_respuesta(reporte.getDescripcion(), reporte.getCreador(),respuesta,reporte.getEstado, schema)

#     @staticmethod
#     def create_reporte_pregunta_from_common(reporte: common.Reporte, pregunta: common.pregunta, schema: Schema) -> common.Reporte:
#         return ReporteService.create_reporte_pregunta(reporte.getDescripcion(), reporte.getCreador(),pregunta,reporte.getEstado, schema)
    
#     @staticmethod
#     def create_reporte_comentario_from_common(reporte: common.Reporte, comentario: common.Comentario, schema: Schema) -> common.Reporte:
#         return ReporteService.create_reporte_comentario(reporte.getDescripcion(), reporte.getCreador(),comentario,reporte.getEstado, schema)
    
#     @staticmethod
#     def create_reporte_respuesta(descripcion: str, creador: str,respuesta: common.Respuesta, estado: reportstatus,schema: Schema) -> common.Reporte:
#         session: Session = Schema.new_session()
#         out: common.Reporte = None
#         try:
#             new_reporte: ReporteRespuesta = ReportesRespuestas.create(session,descripcion, respuesta,creador, estado)
#             out = common.Reporte(new_reporte.descripcion,
#             new_reporte.creador,
#             new_reporte.elemento,new_reporte.estado, new_reporte.id)
#         except Exception as ex:
#             raise ex
#         finally:
#             Schema.remove_session()
#         return out
    
#     @staticmethod
#     def create_reporte_comentario(descripcion: str, creador: str,comentario: common.Comentario, estado: reportstatus,schema: Schema) -> common.Reporte:
#         session: Session = Schema.new_session()
#         out: common.Reporte = None
#         try:
#             new_reporte: ReporteComentario = ReportesComentarios.create(session,descripcion, comentario,creador, estado)
#             out = common.Reporte(new_reporte.descripcion,
#             new_reporte.creador,
#             new_reporte.elemento,new_reporte.estado, new_reporte.id)
#         except Exception as ex:
#             raise ex
#         finally:
#             Schema.remove_session()
#         return out

#     @staticmethod
#     def exists_reporte_pregunta(id:int,schema: Schema):
#         session: Session = schema.new_session()
#         reporte_exists: bool = ReportesPreguntas.get_reporte(session,id)
#         Schema.remove_session()
#         return reporte_exists

#     @staticmethod
#     def exists_reporte_respuesta(id:int,schema: Schema):
#         session: Session = schema.new_session()
#         reporte_exists: bool = ReportesRespuestas.get_reporte(session,id)
#         Schema.remove_session()
#         return reporte_exists

#     @staticmethod
#     def exists_reporte_comentario(id:int, schema: Schema):
#         session: Session = schema.new_session()
#         reporte_exists: bool = ReportesComentarios.get_reporte(session,id)
#         Schema.remove_session()
#         return reporte_exists


#     @staticmethod
#     def list_reportes_preguntas(schema: Schema) -> List[common.Reporte]:
#         out: List[common.Reporte] = []
#         session: Session = schema.new_session()
#         reportes: List[ReportePreguntas] = ReportesPreguntas.list_all(session)
#         for reporte in reportes:
#             out.append(common.Reporte(reporte.descripcion,reporte.creador,reporte.elemento,reporte.estado,reporte.id))
#         Schema.remove_session()
#         return out
    
#     @staticmethod
#     def list_reportes_respuestas(schema: Schema) -> List[common.Reporte]:
#         out: List[common.Reporte] = []
#         session: Session = schema.new_session()
#         reportes: List[ReporteRespuesta] = ReportesRespuestas.list_all(session)
#         for reporte in reportes:
#             out.append(common.Reporte(reporte.descripcion,reporte.creador,reporte.elemento,reporte.estado,reporte.id))
#         Schema.remove_session()
#         return out

#     @staticmethod
#     def list_reportes_comentarios(schema: Schema) -> List[common.Reporte]:
#         out: List[common.Reporte] = []
#         session: Session = schema.new_session()
#         reportes: List[ReporteComentario] = ReportesComentarios.list_all(session)
#         for reporte in reportes:
#             out.append(common.Reporte(reporte.descripcion,reporte.creador,reporte.elemento,reporte.estado,reporte.id))
#         Schema.remove_session()
#         return out