from datetime import datetime
from typing import Optional

from dms2223common.data.Comentario import Comentario

class Respuesta :

    def __init__(self, creador:str, descripcion:str,id:int=None):
        self.__id:Optional[int] = id
        self.__creador:str = creador
        self.__fechaCreacion:datetime = datetime.now()
        self.__descripcion:str = descripcion
        self.__visible:bool = True
        self.__votos:int = 0
        self.__comentarios:dict[int,Comentario] = {}
        self.__votantes:list[str] =[]

    def getId(self) -> Optional[int]:
        return self.__id

    def getCreador(self) -> str:
        return self.__creador

    def getFechaCreacion(self) -> datetime:
        return self.__fechaCreacion
    
    def getDescripcion(self) -> str:
        return self.__descripcion

    # visibilidad respuesta
    def cambiarVisible(self):
        self.__visible = not self.__visible
    
    def getVisible(self) -> bool:
        return self.__visible

    def getVotos(self) -> int:
        return self.__votos

    def votar(self):
        self.__votos+=1

    #crear comentario
    def addComentario(self, comentario: Comentario):
        id = comentario.getId()
        if id is not None:
            self.__comentarios[id]=comentario

    def getComentarios(self) -> dict[int,Comentario]:
        return self.__comentarios
    
    def getVotantes(self) -> list[str]:
        return self.__votantes

    def addVotantes(self,votante:str):
        self.__votantes.append(votante)
    