from typing import Dict
from sqlalchemy import Table, MetaData, Column, String , Integer, TIME, DATE ,ForeignKey,Boolean # type: ignore
from sqlalchemy.orm import relationship  # type: ignore
from dms2223backend.data.db.results.resultbase import ResultBase
# from dms2223backend.data.db.results.reporteDB import Reporte
#from dms2223backend.data.db.results.votosDB import Votos

class ReporteRespuesta(ResultBase):
    """ Definition and storage of comment records.
    """

    def __init__(self, descripcion: str, id_respuesta: int):
        """ Constructor method.
        Initializes a answer record.
        Args:
            - id_pregunta (int): A int with the question's id.
            - content (str): A string with the answer of a question
        """
        
        self.descripcion: str = descripcion
        self.id_respuesta: int = id_respuesta    # @staticmethod
    # def _mapping_properties() -> Dict:
    #     """ Gets the mapping properties dictionary.
    #     Returns:
    #         - Dict: A dictionary with the mapping properties.
    #     """
    #     return {
    #         'comentarios': relationship(Comentario, backref='respuesta'),
    #         'votos': relationship(Votos , backref = 'respuesta'),
    #         'reporte': relationship(Reporte , backref = 'respuesta'), 
    #         #no se que poner en backref
    #     }
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
            'reportePreguntas',
            metadata,
            Column('id', Integer, autoincrement='auto', primary_key=True), 
            Column('creador',String(32),ForeignKey('username'),nullable=False ),          
            Column('descripcion', String(500), nullable=False),
            Column('id_pregunta', Integer, ForeignKey('preguntas.id'), nullable=False),
            Column('fechaCreación', DATE, nullable=False),
            Column('horaCreacion', TIME, nullable=False),
            Column('estado',String,nullable=False) #debe ser la enum, si aceptado,rechazado o pendiente
            
        )
    # @staticmethod
    # def _mapping_properties() -> Dict:
    #     # Definimos la "relación" entre comentarios y votos
    #     return {
    #         'votos': relationship(Votos, backref='id'),
    #         'reportes': relationship(Reporte, backref='id') #añadir votos y backref
    #     }

