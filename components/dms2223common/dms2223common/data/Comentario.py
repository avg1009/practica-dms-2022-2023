from datetime import datetime

from dms2223common.data.sentiment import Sentiment
class Comentario:

    

    def __init__(self, creador:str, descripcion:str, sentimiento: Sentiment,id:int = None):
        self.__id:int = id
        self.__creador:str = creador
        self.__descripcion: str= descripcion
        self.__fechaCreacion:datetime = datetime.now()
        self.__visible:bool= True
        self.__votos:int= 0
        self.__sentimiento: Sentiment =sentimiento
        self.__votantes:list[str] =[]

    def getId(self) -> int:
        return self.__id

    def getCreador(self) -> str:
        return self.__creador

    def getDescripcion(self) -> str:
        return self.__descripcion

    def getFechaCreacion(self) -> datetime:
        return self.__fechaCreacion

    def cambiarVisible(self):
        self.__visible = not self.__visible
    
    def getVisible(self) -> bool:
        return self.__visible

    def votar(self):
        self.__votos+=1
    
    def getVotos(self) -> int:
        return self.__votos 

    def getSentimiento(self) -> Sentiment:
        return self.__sentimiento

    def setSentimiento(self,sentimiento):
        self.__sentimiento=sentimiento

    def getVotantes(self) -> list[str]:
        return self.__votantes

    def addVotantes(self,votante):
        self.__votantes.append(votante)