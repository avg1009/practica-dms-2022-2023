from typing import Dict
from sqlalchemy import Table, MetaData,ForeignKey, Column, String , Integer, TIME, DATE, Boolean # type: ignore
from sqlalchemy.orm import relationship  # type: ignore
from dms2223backend.data.db.results.resultbase import ResultBase
from dms2223backend.data.db.results.respuestaDB import Respuesta
from dms2223backend.data.db.results.reporteDB import Reporte 
class Pregunta(ResultBase):
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
            'preguntas',
            metadata,
            Column('id', Integer, autoincrement='auto', primary_key=True),
            Column('creador',String(32),ForeignKey('username'),nullable=False ),
            Column('titulo', String(100), nullable=False),
            Column('descripcion', String(500), nullable=False),
            Column('fechaCreación', DATE, nullable=False),
            Column('horaCreacion', TIME, nullable=False),
            Column('visible',Boolean,nullable=False),
            Column('respuestas',String(32),ForeignKey('respuestas'),nullable=False),#referencia a tabla respuestas
            Column('reportes',String(32),ForeignKey('reportes'),nullable=False),
                      
         
            

        )

    @staticmethod
    def _mapping_properties() -> Dict:
        """ Gets the mapping properties dictionary.
        Returns:
            - Dict: A dictionary with the mapping properties.
        """
        return {
            'respuestas': relationship(Respuesta, backref='pregunta'),
            'reportes': relationship(Reporte, backref='pregunta')
           

        }