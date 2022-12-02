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
            new_user: Pregunta = Preguntas.create(session, titulo, descripcion)
            out['username'] = new_user.username
        except Exception as ex:
            raise ex
        finally:
            Schema.remove_session()
        return out

    @staticmethod
    def exists_preguna(titulo:str,descripcion:str):
        session: Session = Schema.new_session()
        user_exists: bool = Preguntas.get_pregunta(session, titulo, descripcion)
        Schema.remove_session()
        return user_exists

    @staticmethod
    def list_users():
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
