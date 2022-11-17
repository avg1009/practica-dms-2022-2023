from datetime import datetime

class Respuesta :
    def __init__(self, creador = "", descripcion = ""):
        self.creador = creador
        self.fechaCreacion = datetime.now()
        self.descripcion = descripcion
        self.visible = True
        self.votos = 0
        self.comentarios = list()

    def getCreador(self):
        return self.creador

    def getFechaCreacion(self):
        return self.fechaCreacion
    
    def getDescripcion(self):
        return self.descripcion

    def setDescripcion(self):
        self.descripcion = self.descripcion

    # votar respuesta
    def votarRespuesta(self):
        self.votos += 1
    
    def getVotos(self):
        return self.votos

    # visibilidad respuesta
    def cambiarVisible(self,visible):
        self.visible = not self.visible
    
    def getVisible(self):
        return self.visible

    #crear comentario
    def crearComentario(self, comentario):
        self.comentarios.append(comentario)