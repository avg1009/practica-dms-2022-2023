from typing import List, Dict
from sqlalchemy.orm.session import Session
from dms2223backend.data.db.schema import Schema  # type: ignore
from dms2223backend.data.db.results import Voto
from dms2223backend.data.db.resultsets import Votos
#TODO
class votoService:

    @staticmethod
    def create_voto(descripcion: str, id_respuesta: int):
        session: Session = Schema.new_session()
        out: Dict = {}
        try:
            new_voto: Voto = Votos.create(session, descripcion, id_respuesta)
            out['id'] = new_voto.id
            out['descripcion']=new_voto.descripcion
            out['id_respuesta']=new_voto.id_respuesta
        except Exception as ex:
            raise ex
        finally:
            Schema.remove_session()
        return out

    @staticmethod
    def exists_voto(id:int):
        session: Session = Schema.new_session()
        voto_exists: bool = Votos.get_voto(session,id)
        Schema.remove_session()
        return voto_exists

    @staticmethod
    def list_votos():
        out: List[Dict] = []
        session: Session = Schema.new_session()
        votos: List[voto] = Votos.list_all(session)
        for voto in votos:
            out.append({
                'id': voto.id,
                'descripcion': voto.descripcion,
                'id_respuesta': voto.id_respuesta
            })
        Schema.remove_session()
        return out