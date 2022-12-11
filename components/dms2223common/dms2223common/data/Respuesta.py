from datetime import datetime
from typing import Optional,Dict,List
from dms2223common.data.Comentario import Comentario


class Respuesta :

    def __init__(self, creador:str, descripcion:str,id:Optional[int]=None,fecha:Optional[str]=datetime.now().isoformat()):
        self.__id:Optional[int] = id
        self.__creador:str = creador
        self.__fechaCreacion:datetime = datetime.fromisoformat(fecha)
        self.__descripcion:str = descripcion
        self.__visible:bool = True
        self.__votos:int = 0
        self.__comentarios:List[Comentario] = []
        self.__votantes:List[str] =[]

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
            self.__comentarios.append(comentario)

    def getComentarios(self) -> Dict[int,Comentario]:
        return self.__comentarios
    
    def getVotantes(self) -> List[str]:
        return self.__votantes

    def addVotantes(self,votante:str):
        self.__votantes.append(votante)
    
    def to_json(self,comentarios=True) -> Dict:
        dict={}
        dict["id"]=self.__id
        dict["creador"]=self.__creador
        dict["fecha_creacion"]=self.__fechaCreacion.isoformat()
        dict["descripcion"]=self.__descripcion
        dict["visible"]=self.__visible
        dict["votos"]=self.__votos
        if comentarios:
            com=[]
            for c in self.__comentarios:
                com.append(c.to_json())
            dict["comentarios"]=com
        dict["votantes"]=self.__votantes

        return dict

    def from_json(dict):
        respuesta = Respuesta(dict["creador"],dict["descripcion"],dict["id"])
        respuesta.__fechaCreacion=datetime.fromisoformat(dict["fecha_creacion"])
        respuesta.__visible=dict["visible"]
        respuesta.__votos=dict["votos"]
        for c in dict["comentarios"]:
            comentario = Comentario.from_json(c)
            respuesta.addComentario(comentario)
        respuesta.__votantes=dict["votantes"]

        return respuesta