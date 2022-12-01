from datetime import datetime
from typing import Optional,Dict

from dms2223common.data.Respuesta import Respuesta
class Pregunta:

    
    
    def __init__(self, creador:str, titulo:str, descripcion:str,id:Optional[int]=None):
        self.__id:Optional[int] = id
        self.__creador:str = creador
        self.__titulo: str = titulo
        self.__descripcion: str = descripcion
        self.__fechaCreacion:datetime = datetime.now()
        self.__visible:bool = True
        self.__respuestas:Dict[int,Respuesta] = {}
        self.__reporte = False

    def getId(self) -> Optional[int]:
        return self.__id

    def getCreador(self) -> str:
        return self.__creador

    def getTitulo(self) -> str:
        return self.__titulo

    def getDescripcion(self) -> str:
        return self.__descripcion

    def getFechaCreacion(self) -> datetime:
        return self.__fechaCreacion
    
    def getVisible(self) -> bool:
        return self.__visible

    def cambiarVisible(self):
        self.__visible = not self.__visible
    
    def getRespuestas(self) -> dict[int,Respuesta]:
        return self.__respuestas
    
    def addRespuesta(self,respuesta:Respuesta):
        id = respuesta.getId()
        if id is not None:
            
            self.__respuestas[id]=respuesta
    
    def removeRespuesta(self,respuesta:Respuesta):
        id = respuesta.getId()
        if id is not None:
            self.__respuestas.pop(id)
    
    def getReporte(self) -> bool:
        return self.__reporte

    def reportar(self):
        self.__reporte = True