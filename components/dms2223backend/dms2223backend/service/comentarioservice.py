from typing import List
from sqlalchemy.orm.session import Session
from dms2223backend.data.db.schema import Schema  # type: ignore
from dms2223backend.data.db.results import Comentario
from dms2223backend.data.db.resultsets import Comentarios
import dms2223common.data.Comentario as common
from dms2223common.data.sentiment import Sentiment
class ComentarioService:

    @staticmethod
    def create_comentario(descripcion: str, id_respuesta: int) -> common.Comentario:
        session: Session = Schema.new_session()
        out: common.Comentario
        try:
            new_comentario: Comentario = Comentarios.create(session, descripcion, id_respuesta)
            out = common.Comentario("",new_comentario.descripcion,Sentiment.NEUTRAL,new_comentario.id)
        except Exception as ex:
            raise ex
        finally:
            Schema.remove_session()
        return out

    @staticmethod
    def exists_comentario(id:int) -> bool:
        session: Session = Schema.new_session()
        comentario_exists: bool = Comentarios.get_comentario(session,id)
        Schema.remove_session()
        return comentario_exists

    @staticmethod
    def list_comentarios() -> List[common.Comentario]:
        out: List[common.Comentario] = []
        session: Session = Schema.new_session()
        comentarios: List[Comentario] = Comentarios.list_all(session)
        for comentario in comentarios:
            out.append(common.Comentario("",comentario.descripcion,Sentiment.NEUTRAL,comentario.id))
        Schema.remove_session()
        return out