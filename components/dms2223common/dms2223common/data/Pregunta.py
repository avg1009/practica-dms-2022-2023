from datetime import datetime
import itertools
class Pregunta:

    id_iter= itertools.count()
    
    def __init__(self, creador, titulo, descripcion):
        self.id=next(Pregunta.id_iter)
        self.creador = creador
        self.titulo: str = titulo
        self.descripcion: str = descripcion
        self.fechaCreacion = datetime.now()
        self.visible = True
        self.respuestas = []
        
    def getDescripcion(self):
        return self.descripcion

    def setDescripcion(self,descripcion):
        self.descripcion=descripcion

    def getCreador(self):
        return self.creador

    def getTitulo(self):
        return self.titulo

    def setTitulo(self, titulo):
        self.titulo=titulo

    def getFechaCreacion(self):
        return self.fechaCreacion
    
    def addRespuesta(self,respuesta):
        self.respuestas.append(respuesta)
    
    def removeRespuesta(self,respuesta):
        self.respuestas.remove(respuesta)
    
    def cambiarVisible(self,visible):
        self.visible = not self.visible
    
    def getVisible(self):
        return self.visible

    def getRespuestas(self):
        return self.respuestas
    
    def getId(self):
        return self.id