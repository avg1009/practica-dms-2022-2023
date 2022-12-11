from datetime import datetime
from typing import Dict
from sqlalchemy import Table, MetaData, Column, String , Integer, TIMESTAMP,ForeignKey,Boolean # type: ignore
from sqlalchemy.orm import relationship  # type: ignore
from dms2223backend.data.db.results.resultbase import ResultBase


class VotosComentarios(ResultBase):
    """ Definition and storage of comment records.
    """

    def __init__(self, cantidad:int ,usuario:str,id_comentario:int):
        """ Constructor method.
        Initializes a answer record.
        Args:
            - id_pregunta (int): A int with the question's id.
            - content (str): A string with the answer of a question
        """
        self.id:int
        self.usuario:str = usuario
        self.cantidad:int = cantidad
        self.fechaCreacion:datetime = datetime.now()
        self.id_comentario: int = id_comentario 
        
        
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
            'votosComentarios',
            metadata,
            Column('id', Integer, autoincrement='auto', primary_key=True),
            Column('cantidad',Integer),
            Column('usuario',String(32),nullable=False ),          
            Column('id_comentario', Integer, ForeignKey('comentarios.id'), nullable=False),
            Column('fechaCreación', TIMESTAMP, nullable=False)
        
            
        )
    # @staticmethod
    # def _mapping_properties() -> Dict:
    #     # Definimos la "relación" entre comentarios y votos
    #     return {
    #         'votos': relationship(Votos, backref='id'),
    #         'reportes': relationship(Reporte, backref='id') #añadir votos y backref
    #     }

