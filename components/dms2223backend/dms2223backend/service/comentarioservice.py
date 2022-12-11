from typing import List
from sqlalchemy.orm.session import Session
from dms2223backend.data.db.schema import Schema  # type: ignore
from dms2223backend.data.db.results import Comentario
from dms2223backend.data.db.resultsets import Comentarios
import dms2223common.data.Comentario as common
from dms2223common.data.sentiment import Sentiment
class ComentarioService:

    @staticmethod
    def create_comentario(descripcion: str, id_respuesta: int, creador:str, sentimiento: Sentiment) -> common.Comentario:
        session: Session = Schema.new_session()
        out: common.Comentario = None
        try:
            new_comentario: Comentario = Comentarios.create(session, descripcion, id_respuesta, creador, sentimiento)
            out = common.Comentario(new_comentario.creador,new_comentario.descripcion,new_comentario.sentimiento,new_comentario.id)
        except Exception as ex:
            raise ex
        finally:
            Schema.remove_session()
        return out

    @staticmethod
    def create_comentario_from_common(comentario: common.Comentario, id_respuesta: int) -> common.Comentario:
        return ComentarioService.create_comentario(comentario.getDescripcion(), id_respuesta, comentario.getCreador(), comentario.getSentimiento)

    @staticmethod
    def exists_comentario(id:int) -> bool:
        session: Session = Schema.new_session()
        comentario_exists: bool = Comentarios.get_comentario(session,id)
        Schema.remove_session()
        return comentario_exists

    @staticmethod
    def list_comentarios(id_respuesta: int) -> List[common.Comentario]:
        out: List[common.Comentario] = []
        session: Session = Schema.new_session()
        comentarios: List[Comentario] = Comentarios.list_all(session)
        for comentario in comentarios:
            if comentario.id_respuesta== id_respuesta:
                out.append(common.Comentario(comentario.creador,comentario.descripcion,comentario.sentimiento,comentario.id))
        Schema.remove_session()
        return out

    @staticmethod
    def get_comentario(id : int) -> common.Comentario:
        session : Session = Schema.new_session()
        comentario : Comentario = Comentarios.get_comentario(session, id)
        out: common.Comentario = common.Comentario(comentario.creador,comentario.descripcion,comentario.sentimiento,comentario.id)
        Schema.remove_session()
        return out
