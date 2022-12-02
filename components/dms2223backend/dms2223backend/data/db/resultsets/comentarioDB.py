import hashlib
from typing import List
from sqlalchemy.exc import IntegrityError  # type: ignore
from sqlalchemy.orm.session import Session  # type: ignore
from sqlalchemy.orm.exc import NoResultFound  # type: ignore
from dms2223backend.data.db.results.comentarioDB import Comentario
from dms2223backend.data.db.exc import ComentarioExisteError
from dms2223backend.data.db.exc import ComentarioNoExisteError


class Comentarios():
    """ Class responsible of table-level users operations.
    """
    @staticmethod
    def create(session: Session, descripcion: str, id_respuesta: int) -> Comentario:
        """ Creates a new question record.

        Note:
            Any existing transaction will be committed.

        Args:
            - session (Session): The session object.
            - titulo (str): The title of the question
            - descripcion (str): The description of the question

        Raises:
            - ValueError: If either the username or the password_hash is empty.
            - ComentarioExisteError: If a question with the same title already exists.

        Returns:
            - User: The created `User` result.
        """
        if not descripcion or not id_respuesta:
            raise ValueError('A title and a description are required.')
        try:
            nuevo_comentario = Comentario(descripcion, id_respuesta)
            session.add(nuevo_comentario)
            session.commit()
            return nuevo_comentario
        except IntegrityError as ex:
            session.rollback()
            raise ComentarioExisteError(
                'A coment with this id already exists.'
                ) from ex

    @staticmethod
    def list_all(session: Session) -> List[Comentario]:
        """Lists every user.

        Args:
            - session (Session): The session object.

        Returns:
            - List[User]: A list of `User` registers.
        """
        query = session.query(Comentario)
        return query.all()

    @staticmethod
    def get_comentario(session: Session, id: int) -> Optional[Comentario]:
        """ Determines whether a user exists or not.

        Args:
            - session (Session): The session object.
            - id (str): The question id to find
            
        Returns:
            - Optional[Comentario]: The question 
        """
        if not id:
            raise ValueError('An id is requiered.')
        try:
            query = session.query(Comentario).filter_by(id=id)
            comentario: Comentario = query.one()
        except NoResultFound as ex:
            raise ComentarioNoExisteError(
                'The question with title ' + id + ' don\'t exists.'
                ) from ex
        return comentario