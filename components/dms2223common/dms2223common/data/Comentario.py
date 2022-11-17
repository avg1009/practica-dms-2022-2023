from datetime import datetime
class Comentario:

    def __init__(self, creador, descripcion):
        self.creador = creador
        self.descripcion= descripcion
        self.fechaCreacion = datetime.now()
        self.visible= True
        self.votos= 0
        
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

