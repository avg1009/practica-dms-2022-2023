import hashlib
from typing import List, Optional
from sqlalchemy.exc import IntegrityError  # type: ignore
from sqlalchemy.orm.session import Session  # type: ignore
from sqlalchemy.orm.exc import NoResultFound  # type: ignore
from dms2223backend.data.db.results.reporteDB import Reporte
from dms2223backend.data.db.exc import ReporteExisteError
from dms2223backend.data.db.exc import ReporteNoExisteError


class Reportes():
    """ Class responsible of table-level users operations.
    """
    @staticmethod
    def create(session: Session, titulo: str, descripcion: str) -> Reporte:
        """ Creates a new question record.

        Note:
            Any existing transaction will be committed.

        Args:
            - session (Session): The session object.
            - titulo (str): The title of the question
            - descripcion (str): The description of the question

        Raises:
            - ValueError: If either the username or the password_hash is empty.
            - ReporteExisteError: If a question with the same title already exists.

        Returns:
            - User: The created `User` result.
        """
        if not titulo or not descripcion:
            raise ValueError('A title and a description are required.')
        try:
            nuevo_reporte = Reporte(titulo, descripcion)
            session.add(nuevo_reporte)
            session.commit()
            return nuevo_reporte
        except IntegrityError as ex:
            session.rollback()
            raise ReporteExisteError(
                'A question with title ' + titulo + ' already exists.'
                ) from ex

    @staticmethod
    def list_all(session: Session) -> List[Reporte]:
        """Lists every user.

        Args:
            - session (Session): The session object.

        Returns:
            - List[User]: A list of `User` registers.
        """
        query = session.query(Reporte)
        return query.all()

    @staticmethod
    def get_reporte(session: Session, id: int) -> Optional[Reporte]:
        """ Determines whether a user exists or not.

        Args:
            - session (Session): The session object.
            - id (str): The question id to find
            
        Returns:
            - Optional[Reporte]: The question 
        """
        if not id:
            raise ValueError('An id is requiered.')
        try:
            query = session.query(Reporte).filter_by(id=id)
            reporte: Reporte = query.one()
        except NoResultFound as ex:
            raise ReporteNoExisteError(
                'The question with title ' + id + ' don\'t exists.'
                ) from ex
        return reporte