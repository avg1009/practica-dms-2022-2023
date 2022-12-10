from typing import Dict
from sqlalchemy import Table, MetaData, Column, String , Integer, TIME, DATE # type: ignore
from sqlalchemy.orm import relationship  # type: ignore
from dms2223backend.data.db.results.resultbase import ResultBase
from dms2223backend.data.db.results.respuestaDB import Respuesta

class Reporte(ResultBase):
    """ Definition and storage of discussion records.
    """

    def __init__(self, title: str, content: str):
        """ Constructor method.
        Initializes a discussion record.
        Args:
            - title (str): A string with the discussion title.
            - content (str): A string with the discussion title.
        """

      
        self.title: str = title
        self.content: str = content
        self.id:int

    @staticmethod
    def _table_definition(metadata: MetaData) -> Table:
        """ Gets the table definition.
        Args:
            - metadata (MetaData): The database schema metadata
                        (used to gather the entities' definitions and mapping)
        
        Returns:
            - Table: A `Table` object with the table definition.
        """
        return Table(
            'reportes',
            metadata,
            Column('id', Integer, autoincrement='auto', primary_key=True),
            Column('descripcion', String(500), nullable=False)
        )

    @staticmethod
    def _mapping_properties() -> Dict:
        """ Gets the mapping properties dictionary.
        Returns:
            - Dict: A dictionary with the mapping properties.
        """
        return {
            #'respuestas': relationship(Respuesta, backref='pregunta')#no se que poner en backref

        }