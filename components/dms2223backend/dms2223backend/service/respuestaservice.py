from typing import List, Dict
from sqlalchemy.orm.session import Session
from dms2223backend.data.db.schema import Schema  # type: ignore
from dms2223backend.data.db.results import Respuesta
from dms2223backend.data.db.resultsets import Respuestas

class RespuestaService:

    @staticmethod
    def create_respuesta(descripcion: str, id_pregunta: int):
        session: Session = Schema.new_session()
        out: Dict = {}
        try:
            new_respuesta: Respuesta = Respuestas.create(session, descripcion, id_pregunta)
            out['id'] = new_respuesta.id
            out['descripcion']=new_respuesta.descripcion
            out['id_pregunta']=new_respuesta.id_pregunta
        except Exception as ex:
            raise ex
        finally:
            Schema.remove_session()
        return out

    @staticmethod
    def exists_respuesta(descripcion:str,id:int):
        session: Session = Schema.new_session()
        respuesta_exists: bool = Respuestas.get_respuesta(session,id)
        Schema.remove_session()
        return respuesta_exists

    @staticmethod
    def list_respuestas():
        out: List[Dict] = []
        session: Session = Schema.new_session()
        Respuestas: List[Respuesta] = Respuestas.list_all(session)
        for respuesta in Respuestas:
            out.append({
                'id': respuesta.id,
                'descripcion': respuesta.descripcion,
                'id_pregunta': respuesta.id_pregunta
            })
        Schema.remove_session()
        return out