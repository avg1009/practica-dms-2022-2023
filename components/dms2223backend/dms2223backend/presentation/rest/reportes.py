# from typing import List, Dict
# from http import HTTPStatus
# from flask import current_app
# from dms2223backend.service import reporteservice
# from dms2223backend.service import preguntaservice
# from dms2223backend.service import respuestaservice
# from dms2223backend.service import comentarioservice
# import dms2223common.data.Respuesta as common
# import dms2223common.data.Pregunta as common
# import dms2223common.data.Comentario as common
# import dms2223common.data.Reporte as common

# def post_reporte_pregunta(reporte: common.Reporte, pregunta: common.Pregunta):
#     with current_app.app_context() :
#         if preguntaservice.PreguntaService.exits_pregunta(pregunta.getId()):
#             return reporteservice.ReporteService.create_reporte_pregunta_from_common(
#                 reporte,pregunta, current_app.db), HTTPStatus.OK.value
#         else:
#             return ("La pregunta no existe", HTTPStatus.NOT_FOUND.value)

# def get_reportes_preguntas():
#     with current_app.app_context() :
#         return reporteservice.ReporteService.list_reportes_preguntas(current_app.db),HTTPStatus.OK.value
#     pass

# def set_status_pregunta(qrid: int):
#     pass

# def post_reporte_respuesta(reporte: common.Reporte, respuesta: common.Respuesta):
#     with current_app.app_context() :
#         if respuestaservice.RespuestaService.exits_respuesta(respuesta.getId()):
#             return reporteservice.ReporteService.create_reporte_respuesta_from_common(
#                 reporte,respuesta, current_app.db), HTTPStatus.OK.value
#         else:
#             return ("La pregunta no existe", HTTPStatus.NOT_FOUND.value)

# def get_reportes_respuestas():
#     with current_app.app_context() :
#         return reporteservice.ReporteService.list_reportes_respuestas(current_app.db),HTTPStatus.OK.value
# def set_status_respuesta(arid: int):
#     pass

# def post_reporte_comentario(reporte: common.Reporte, comentario: common.Comentario):
#     with current_app.app_context() :
#         if comentarioservice.ComentarioService.exits_comentario(comentario.getId()):
#             return reporteservice.ReporteService.create_reporte_comentario_from_common(
#                 reporte,comentario, current_app.db), HTTPStatus.OK.value
#         else:
#             return ("La pregunta no existe", HTTPStatus.NOT_FOUND.value)

# def get_reportes_comentarios():
#     with current_app.app_context() :
#         return reporteservice.ReporteService.list_reportes_comentarios(current_app.db),HTTPStatus.OK.value
    

# def set_status_comentario(crid: int):
#     pass