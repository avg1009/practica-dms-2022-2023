from ast import List
import datetime
from typing import Dict, Optional
from sqlalchemy import Table,TIMESTAMP, MetaData, Column, String , Integer,Enum ,ForeignKey,Boolean # type: ignore
from sqlalchemy.orm import relationship  # type: ignore
from dms2223backend.data.db.results.resultbase import ResultBase
from dms2223common.data.sentiment import Sentiment
from datetime import datetime


class Comentario(ResultBase):
    """ Definition and storage of comment records.
    """

    def __init__(self, descripcion:str, id_respuesta:int, creador:str, sentimiento: Sentiment):
        self.id:int 
        self.id_respuesta:int = id_respuesta
        self.creador:str = creador
        self.descripcion: str= descripcion
        #self.fechaCreacion:datetime = datetime.now()
        self.visible:bool= True
        self.sentimiento: Sentiment =sentimiento 

        
        
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
            'comentarios',
            metadata,
            Column('id', Integer, autoincrement='auto', primary_key=True), 
            Column('id_respuesta', Integer, ForeignKey('respuestas.id'), nullable=False),
            Column('creador',String(32),nullable=False ),          
            Column('descripcion', String(500), nullable=False),
            #Column('fechaCreación', TIMESTAMP, nullable=False),
            Column('visible',Boolean,nullable=False),
            Column('sentimiento',Enum(Sentiment),default = Sentiment.NEUTRAL.name,nullable=False)  
        )
    # @staticmethod
    # def _mapping_properties() -> Dict:
    #     # Definimos la "relación" entre comentarios y votos
    #     return {
    #         #'comentarios': relationship(Respuesta, backref='pregunta')
    #         #'votos': relationship(Votos, backref='id'),
    #         #'reportes': relationship(Reporte, backref='id') #añadir votos y backref
    #     }

