
class Pregunta:

    def __init__(self, descripcion):
        self.descripcion= descripcion
        self.visible= True
        self.respuestas=[]

    def getDescripcion(self):
        return self.descripcion

    def setDescripcion(self,descripcion):
        self.descripcion=descripcion
    
    def addRespuesta(self,respuesta):
        self.respuestas.append(respuesta)
    
    def removeRespuesta(self,respuesta):
        self.respuestas.remove(respuesta)
    
    def setVisible(self,visible):
        self.visible=visible
    
    def getVisible(self):
        return self.visible

    def getRespuestas(self):
        return self.respuestas