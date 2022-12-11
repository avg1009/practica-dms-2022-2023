from datetime import datetime
from typing import Dict
from sqlalchemy import Table, MetaData, Column, String ,Boolean, Integer, TIMESTAMP ,ForeignKey # type: ignore
from sqlalchemy.orm import relationship  # type: ignore
from dms2223backend.data.db.results.resultbase import ResultBase
from dms2223backend.data.db.results.comentarioDB import Comentario
# from dms2223backend.data.db.results.votosDB import Votos
# from dms2223backend.data.db.results.reporteDB import Reporte

class Respuesta(ResultBase):
    """ Definition and storage of answer records.
    """

    
   
        
       
    def __init__(self, descripcion:str,id_pregunta:int, creador:str):
        self.id:int 
        self.id_pregunta:int = id_pregunta
        self.creador:str = creador
        self.fechaCreacion:datetime = datetime.now()
        self.descripcion:str = descripcion
        self.visible:bool = True
  
        
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
            Column('id_pregunta', Integer, ForeignKey('preguntas.id'), nullable=False),
            Column('creador',String(32),nullable=False ), 
            Column('fechaCreación', TIMESTAMP, nullable=False),          
            Column('descripcion', String(500), nullable=False),
            Column('visible',Boolean,nullable=False),
           
        )


    @staticmethod
    def _mapping_properties() -> Dict:
        """ Gets the mapping properties dictionary.
        Returns:
            - Dict: A dictionary with the mapping properties.
        """
        return {
            'comentarios': relationship(Comentario, backref='respuesta'),
           # 'votos': relationship(Votos , backref = 'respuesta'),
           # 'reporte': relationship(Reporte , backref = 'respuesta'), 
            #no se que poner en backref
        }
