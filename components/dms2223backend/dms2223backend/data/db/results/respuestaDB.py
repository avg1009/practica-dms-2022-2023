from typing import Dict
from sqlalchemy import Table, MetaData, Column, String , Integer, TIME, DATE ,ForeignKey # type: ignore
from sqlalchemy.orm import relationship  # type: ignore
from dms2223backend.data.db.results.resultbase import ResultBase
from dms2223backend.data.db.results.preguntaDB import Pregunta

class Respuesta(ResultBase):
    """ Definition and storage of answer ORM records.
    """

    def __init__(self, id: int, content: str):
        """ Constructor method.
        Initializes a answer record.
        Args:
            - id (int): A int with the discussion's id.
            - content (str): A string with the answer of a question
        """
        
        self.id: str = id
        self.content: str = content
        
        
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
            'respuestas',
            metadata,
            Column('id', Integer, autoincrement='auto', primary_key=True),            
            Column('descripcion', String(500), nullable=False),
            Column('id_pregunta', Integer, ForeignKey('preguntas.id'), nullable=False)
            # Column('time', TIME, nullable = False),
            # Column('date', DATE, nullable = False)
        )
