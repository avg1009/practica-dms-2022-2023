from typing import List, Dict
from sqlalchemy.orm.session import Session
from dms2223backend.data.db.schema import Schema  # type: ignore
from dms2223backend.data.db.results import Pregunta
from dms2223backend.data.db.resultsets import Preguntas
import dms2223common.data.Pregunta as common
class PreguntaService():

    @staticmethod
    def create_pregunta(titulo: str, descripcion: str) -> common.Pregunta:
        session: Session = Schema.new_session()
        out: common.Pregunta
        try:
            new_pregunta: Pregunta = Preguntas.create(session, titulo, descripcion)
            out= common.Pregunta("",new_pregunta.title,new_pregunta.content,new_pregunta.id)
        except Exception as ex:
            raise ex
        finally:
            Schema.remove_session()
        return out

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
            out.append(common.Pregunta("",pregunta.title,pregunta.content,pregunta.id))
        Schema.remove_session()
        return out
