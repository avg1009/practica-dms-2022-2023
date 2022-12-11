from datetime import datetime
import json
from typing import Dict, Optional,List
from flask import current_app
from dms2223common.data.sentiment import Sentiment
class Comentario:

    

    def __init__(self, creador:str, descripcion:str, sentimiento: Sentiment,id:Optional[int] = None,fecha:Optional[str]=datetime.now().isoformat()):
        self.__id:Optional[int] = id
        self.__creador:str = creador
        self.__descripcion: str= descripcion
        self.__fechaCreacion:datetime = datetime.fromisoformat(fecha)
        self.__visible:bool= True
        self.__votos:int= 0
        self.__sentimiento: Sentiment =sentimiento
        self.__votantes:List[str] =[]

    def getId(self) -> Optional[int]:
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

    def getVotantes(self) -> List[str]:
        return self.__votantes

    def addVotantes(self,votante):
        self.__votantes.append(votante)

    def to_json(self) -> Dict:
        dict = {}
        dict["id"]=self.__id
        dict["creador"]=self.__creador
        dict["descripcion"]=self.__descripcion
        dict["fecha_creacion"]=self.__fechaCreacion.isoformat()
        dict["visible"]=self.__visible
        dict["votos"]=self.__votos
        dict["sentimiento"]=self.__sentimiento.value
        dict["votantes"]=self.__votantes
        return dict

    def from_json(dict):
        comentario = Comentario(dict["creador"],dict["descripcion"],dict["sentimiento"] ,dict["id"])
        
        comentario.__fechaCreacion=datetime.fromisoformat(dict["fecha_creacion"])
        comentario.__visible=dict["visible"]
        comentario.__votos=dict["votos"]
        
        comentario.__votantes=dict["votantes"]
        return comentario