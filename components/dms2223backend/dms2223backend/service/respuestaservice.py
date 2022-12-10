from typing import List, Dict
from sqlalchemy.orm.session import Session
from dms2223backend.data.db.schema import Schema  # type: ignore
from dms2223backend.data.db.results import Respuesta
from dms2223backend.data.db.resultsets import Respuestas
import dms2223common.data.Respuesta as common
class RespuestaService:

    @staticmethod
    def create_respuesta(descripcion: str, id_pregunta: int) -> common.Respuesta:
        session: Session = Schema.new_session()
        out: common.Respuesta
        try:
            new_respuesta: Respuesta = Respuestas.create(session, descripcion, id_pregunta)
            out= common.Respuesta("",new_respuesta.descripcion,new_respuesta.id)
        except Exception as ex:
            raise ex
        finally:
            Schema.remove_session()
        return out

    @staticmethod
    def exists_respuesta(id:int):
        session: Session = Schema.new_session()
        respuesta_exists: bool = Respuestas.get_respuesta(session,id)
        Schema.remove_session()
        return respuesta_exists

    # @staticmethod
    # def list_respuestas():
    #     out: List[common.Respuesta] = []
    #     session: Session = Schema.new_session()
    #     respuestas: List[Respuesta] = Respuestas.list_all(session)
    #     for respuesta in respuestas:
    #         out.append(common.Respuesta("",respuesta.descripcion,respuesta.id))
    #     Schema.remove_session()
    #     return out

    @staticmethod
    def list_respuestas(id_pregunta: int):
        out: List[common.Respuesta] = []
        session: Session = Schema.new_session()
        respuestas: List[Respuesta] = Respuestas.list_all(session)
        for respuesta in respuestas:
            if respuesta.id_pregunta== id_pregunta:
                out.append(common.Respuesta("",respuesta.descripcion,respuesta.id))
        Schema.remove_session()
        return out
    
    @staticmethod
    def get_respuesta(id : int) :
        session : Session = Schema.new_session()
        respuesta : Respuesta = Respuestas.get_respuesta(session, id)
        Schema.remove_session()
        return respuesta

    @staticmethod
    def poner_voto (aid : int) :
        pass