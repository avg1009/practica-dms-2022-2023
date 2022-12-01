from datetime import datetime
from typing import Optional

from dms2223common.data.reportstatus import ReportStatus
from dms2223common.data.Comentario import Comentario
from dms2223common.data.Pregunta import Pregunta
from dms2223common.data.Respuesta import Respuesta

class Reporte:


    def __init__(self, descripcion:str, autor:str, elemento, estado:ReportStatus, id:Optional[int]= None):
        self.__id:Optional[int] = id
        self.__descripcion: str = descripcion
        self.__autor:str = autor
        self.__fechaReporte:datetime = datetime.now()
        self.__elemento = elemento
        self.__estado: ReportStatus = estado
        if ( isinstance(elemento,Pregunta) ):
            self.__tipoElemento = "pregunta"
        elif ( isinstance(elemento,Respuesta) ):
            self.__tipoElemento = "respuesta"
        elif ( isinstance(elemento,Comentario) ):
            self.__tipoElemento = "comentario"

    def getId(self) -> Optional[int]:
        return self.__id

    def getDescripcion(self) -> str:
        return self.__descripcion
    
    def getAutor(self) -> str:
        return self.__autor
    
    def getFechaReporte(self) -> datetime:
        return self.__fechaReporte
    
    def getElemento(self):
        return self.__elemento

    def setEstado(self,estado):
        self.__estado=estado
    
    def getEstado(self) -> ReportStatus:
        return self.__estado

    def getTipoElemento(self) -> str:
        return self.__tipoElemento