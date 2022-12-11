from typing import List, Dict
from sqlalchemy.orm.session import Session
from dms2223backend.data.db.schema import Schema  # type: ignore
from dms2223backend.data.db.results import Pregunta
from dms2223backend.data.db.resultsets import Preguntas
import dms2223common.data.Pregunta as common
class PreguntaService():

    @staticmethod
    def create_pregunta(titulo: str, descripcion: str, creador:str) -> common.Pregunta:
        session: Session = Schema.new_session()
        out: common.Pregunta = None
        try:
            new_pregunta: Pregunta = Preguntas.create(session, titulo, descripcion, creador)
            out= common.Pregunta(new_pregunta.creador,new_pregunta.titulo,new_pregunta.descripcion,new_pregunta.id)
        except Exception as ex:
            raise ex
        finally:
            Schema.remove_session()
        return out
    
    @staticmethod
    def create_pregunta_from_common(pregunta: common.Pregunta) -> common.Pregunta:
        return PreguntaService.create_pregunta(pregunta.getTitulo(), pregunta.getDescripcion(), pregunta.getCreador())

    @staticmethod
    def exists_preguna(id:int):
        session: Session = Schema.new_session()
        pregunta_exists: bool = Preguntas.get_pregunta(session, id)
        Schema.remove_session()
        return pregunta_exists

    @staticmethod
    def list_preguntas() -> List[common.Pregunta]:
        out: List[common.Pregunta] = []
        session: Session = Schema.new_session()
        preguntas: List[Pregunta] = Preguntas.list_all(session)
        for pregunta in preguntas:
            out.append(common.Pregunta(pregunta.creador,pregunta.titulo,pregunta.descripcion,pregunta.id))
        Schema.remove_session()
        return out

    @staticmethod
    def get_pregunta(id : int) -> common.Pregunta:
        session : Session = Schema.new_session()
        pregunta : Pregunta = Preguntas.get_pregunta(session, id)
        out= common.Pregunta(pregunta.creador,pregunta.titulo,pregunta.descripcion,pregunta.id)
        Schema.remove_session()
        return out