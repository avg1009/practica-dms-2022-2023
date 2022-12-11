import hashlib
from typing import List, Optional
from sqlalchemy.exc import IntegrityError  # type: ignore
from sqlalchemy.orm.session import Session  # type: ignore
from sqlalchemy.orm.exc import NoResultFound  # type: ignore
from dms2223backend.data.db.results.votos.votosComentarioDB import VotosComentario
from dms2223backend.data.db.exc import VotoExisteError
from dms2223backend.data.db.exc import VotoNoExisteError


class VotosComentarios():
    """ Class responsible of table-level users operations.
    """
    @staticmethod
    def create(session: Session, usuario:str,id_comentario:int) -> VotosComentario:
        """ Creates a new question record.

        Note:
            Any existing transaction will be committed.

        Args:
            - session (Session): The session object.
            - titulo (str): The title of the question
            - descripcion (str): The description of the question

        Raises:
            - ValueError: If either the username or the password_hash is empty.
            - VotoExisteError: If a question with the same title already exists.

        Returns:
            - User: The created `User` result.
        """
        if not usuario or not id_comentario:
            raise ValueError('A title and a description are required.')
        try:
            nuevo_voto_comentario = VotosComentario(usuario, id_comentario)
            session.add(nuevo_voto_comentario)
            session.commit()
            return nuevo_voto_comentario
        except IntegrityError as ex:
            session.rollback()
            raise VotoExisteError(
                'A vote  with this id already exists.'
                ) from ex

    @staticmethod
    def list_all(session: Session,id_comentario:int) -> List[VotosComentario]:
        """Lists every user.

        Args:
            - session (Session): The session object.

        Returns:
            - List[User]: A list of `User` registers.
        """
        query = session.query(VotosComentario)
        return query.where(VotosComentario.id_comentario == id_comentario)

    @staticmethod
    def get_respuesta(session: Session, id: int) -> Optional[VotosComentario]:
        """ Determines whether a user exists or not.

        Args:
            - session (Session): The session object.
            - id (str): The question id to find
            
        Returns:
            - Optional[VotosComentario]: The question 
        """
        if not id:
            raise ValueError('An id is requiered.')
        try:
            query = session.query(VotosComentario).filter_by(id=id)
            respuesta: VotosComentario = query.one()
        except NoResultFound as ex:
            raise VotoNoExisteError(
                'The vote with id ' + id + ' don\'t exists.'
                ) from ex
        return respuesta