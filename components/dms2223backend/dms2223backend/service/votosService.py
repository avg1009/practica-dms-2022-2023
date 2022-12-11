# from typing import List, Dict
# from sqlalchemy.orm.session import Session
# from dms2223backend.data.db.schema import Schema  # type: ignore
# # from dms2223backend.data.db.resultsets import Votos
# from dms2223backend.data.db.results.votos import VotosComentarios #voto
# from dms2223backend.data.db.results.votos import VotosRespuestas #voto
# # from dms2223backend.data.db.resultsets.votos import VotosComentarios #voto
# # from dms2223backend.data.db.resultsets.votos import VotosRespuestas #voto

# #TODO
# class VotoService:

#     @staticmethod
#     def create_voto_respuesta(id_respuesta: int, schema: Schema):
#         session: Session = schema.new_session()
#         out: Dict = {}
#         try:
#             new_voto: VotosRespuestas = Votos.create(session, id_respuesta)
#             out['id'] = new_voto.id
#             out['id_respuesta'] = new_voto.id_respuesta
#         except Exception as ex:
#             raise ex
#         finally:
#             Schema.remove_session()
#         return out

#     @staticmethod
#     def create_voto_comentario(id_comentario: int, schema: Schema):
#         session: Session = schema.new_session()
#         out: Dict = {}
#         try:
#             new_voto: VotosComentarios = Votos.create(session,id_comentario)
#             out['id'] = new_voto.id
#             out['id_comentario'] = new_voto.id_comentario
#         except Exception as ex:
#             raise ex
#         finally:
#             Schema.remove_session()
#         return out

#     @staticmethod
#     def exists_voto_respuesta(id_respuesta:int, schema: Schema):
#         session: Session = schema.new_session()
#         voto_exists: bool = Votos.get_voto(session,id_respuesta)
#         Schema.remove_session()
#         return voto_exists

#     @staticmethod
#     def exists_voto_comentario(id_comentario:int, schema: Schema):
#         session: Session = schema.new_session()
#         voto_exists: bool = Votos.get_voto(session,id)
#         Schema.remove_session()
#         return voto_exists

#     @staticmethod
#     def list_votos_respuestas(schema: Schema):
#         out: List[Dict] = []
#         session: Session = Schema.new_session()
#         votos: List[VotosRespuestas] = Votos.list_all(session)
#         for voto in votos:
#             out.append({
#                 'id': voto.id,
#                 'cantidad': voto.cantidad,
#                 'id_respuesta': voto.id_respuesta
#             })
#         Schema.remove_session()
#         return out

#     @staticmethod
#     def list_votos_comentarios(schema: Schema):
#         out: List[Dict] = []
#         session: Session = schema.new_session()
#         votos: List[VotosComentarios] = Votos.list_all(session)
#         for voto in votos:
#             out.append({
#                 'id': voto.id,
#                 'cantidad': voto.cantidad,
#                 'id_comentario': voto.id_comentario
#             })
#         Schema.remove_session()
#         return out