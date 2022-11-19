from datetime import datetime
import itertools
class Comentario:
    id_iter=itertools.count()
    def __init__(self, creador, descripcion, respuesta):
        self.id=next(self.id_iter)
        self.creador = creador
        self.descripcion= descripcion
        self.fechaCreacion = datetime.now()
        self.visible= True
        self.votos= 0
        self.respuesta=respuesta
        
    def getDescripcion(self):
        return self.descripcion

    def setDescripcion(self,descripcion):
        self.descripcion=descripcion

    def getCreador(self):
        return self.creador
    
    def getFechaCreacion(self):
        return self.fechaCreacion

    def cambiarVisible(self,visible):
        self.visible = not self.visible
    
    def getVisible(self):
        return self.visible

    def votarComentario(self):
        self.votos+=1
    
    def getVotos(self):
        return self.votos

    def getRespuesta(self):
        return self.respuesta

    def setRespuesta(self,respuesta):
        self.respuesta=respuesta
    
    def getId(self):
        return self.id

