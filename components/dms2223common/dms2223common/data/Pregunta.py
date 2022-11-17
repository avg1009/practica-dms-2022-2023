
import string
from datetime import datetime

class Pregunta:

<<<<<<< HEAD
    def __init__(self, descripcion,autor=""):
=======
    def __init__(self, creador, titulo, descripcion):
        self.creador = creador
        self.titulo = titulo
>>>>>>> a80054d (Añadidos los campos faltantes a las clases)
        self.descripcion: string = descripcion
        self.fechaCreacion = datetime.now()
        self.visible: bool = True
        self.respuestas = []
        self.autor = autor

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