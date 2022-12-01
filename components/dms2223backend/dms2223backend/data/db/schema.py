
""" Schema class module.
"""

from sqlalchemy import create_engine, event  # type: ignore
from sqlalchemy.engine import Engine  # type: ignore
from sqlalchemy.ext.declarative import declarative_base  # type: ignore
from sqlalchemy.orm import sessionmaker, scoped_session  # type: ignore
from sqlalchemy.orm.session import Session  # type: ignore
from dms2223backend.data.config import BackendConfiguration
from dms2223backend.data.db.results import comentarioDB,preguntaDB,reporteDB,respuestaDB,resultbase,votosDB


# Required for SQLite to enforce FK integrity when supported
@event.listens_for(Engine, "connect")
def set_sqlite_pragma(
    dbapi_connection, connection_record
):  # pylint: disable=unused-argument
    """ Sets the SQLite foreign keys enforcement pragma on connection.
    Args:
        - dbapi_connection: The connection to the database API.
    """
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys = ON;")
    cursor.close()

class Schema:
    """ Class responsible of the schema initialization and session generation.
    """
    #TODO
    def __init__(self, config: BackendConfiguration):
        """ Constructor method.
        Initializes the schema, deploying it if necessary.
        Args:
            - config (AuthConfiguration): The instance with the schema connection parameters.
        Raises:
            - RuntimeError: When the connection cannot be created/established.
        """
        
    def new_session(self) -> Session:
        """ Constructs a new session.
        Returns:
            - Session: A new `Session` object.
        """
        return self.__session_maker()

    def remove_session(self) -> None:
        """ Frees the existing thread-local session.
        """
        self.__session_maker.remove()