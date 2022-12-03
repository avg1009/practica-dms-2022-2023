from typing import List, Dict
from sqlalchemy.orm.session import Session
from dms2223backend.data.db.schema import Schema  # type: ignore
from dms2223backend.data.db.results import Comentario
from dms2223backend.data.db.resultsets import Comentarios

class ComentarioService:

    @staticmethod
    def create_comentario(descripcion: str, id_respuesta: int):
        session: Session = Schema.new_session()
        out: Dict = {}
        try:
            new_comentario: Comentario = Comentarios.create(session, descripcion, id_respuesta)
            out['id'] = new_comentario.id
            out['descripcion']=new_comentario.descripcion
            out['id_respuesta']=new_comentario.id_respuesta
        except Exception as ex:
            raise ex
        finally:
            Schema.remove_session()
        return out

    @staticmethod
    def exists_comentario(id:int):
        session: Session = Schema.new_session()
        comentario_exists: bool = Comentarios.get_comentario(session,id)
        Schema.remove_session()
        return comentario_exists

    @staticmethod
    def list_comentarios():
        out: List[Dict] = []
        session: Session = Schema.new_session()
        comentarios: List[Comentario] = Comentarios.list_all(session)
        for comentario in comentarios:
            out.append({
                'id': comentario.id,
                'descripcion': comentario.descripcion,
                'id_respuesta': comentario.id_respuesta
            })
        Schema.remove_session()
        return out