from typing import List, Dict
from sqlalchemy.orm.session import Session
from dms2223backend.data.db.schema import Schema  # type: ignore
from dms2223backend.data.db.results import reporte
from dms2223backend.data.db.resultsets import Reportes
#TODO
class ReporteService:

    @staticmethod
    def create_reporte(descripcion: str, id_respuesta: int):
        session: Session = Schema.new_session()
        out: Dict = {}
        try:
            new_reporte: reporte = Reportes.create(session, descripcion, id_respuesta)
            out['id'] = new_reporte.id
            out['descripcion']=new_reporte.descripcion
            out['id_respuesta']=new_reporte.id_respuesta
        except Exception as ex:
            raise ex
        finally:
            Schema.remove_session()
        return out

    @staticmethod
    def exists_reporte(id:int):
        session: Session = Schema.new_session()
        reporte_exists: bool = Reportes.get_reporte(session,id)
        Schema.remove_session()
        return reporte_exists

    @staticmethod
    def list_reportes():
        out: List[Dict] = []
        session: Session = Schema.new_session()
        reportes: List[reporte] = Reportes.list_all(session)
        for reporte in reportes:
            out.append({
                'id': reporte.id,
                'descripcion': reporte.descripcion,
                'id_respuesta': reporte.id_respuesta
            })
        Schema.remove_session()
        return out