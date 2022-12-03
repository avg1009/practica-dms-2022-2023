from typing import List, Dict
from sqlalchemy.orm.session import Session
from dms2223backend.data.db.schema import Schema  # type: ignore
from dms2223backend.data.db.results import Pregunta
from dms2223backend.data.db.resultsets import Preguntas

class PreguntaService():

    @staticmethod
    def create_pregunta(titulo: str, descripcion: str):
        session: Session = Schema.new_session()
        out: Dict = {}
        try:
            new_pregunta: Pregunta = Preguntas.create(session, titulo, descripcion)
            out['id']= new_pregunta.id
            out['titulo']=new_pregunta.title
            out['descripcion']=new_pregunta.content
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
    def list_preguntas():
        out: List[Dict] = []
        session: Session = Schema.new_session()
        preguntas: List[Pregunta] = Preguntas.list_all(session)
        for pregunta in preguntas:
            out.append({
                'id': pregunta.id,
                'Titulo': pregunta.title,
                'Descripcion': pregunta.content
            })
        Schema.remove_session()
        return out
