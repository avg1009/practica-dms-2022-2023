class Comentario:

    def __init__(self, descripcion):
        self.descripcion= descripcion
        self.visible= True
        self.votos= 0
        
    def getDescripcion(self):
        return self.descripcion

    def setDescripcion(self,descripcion):
        self.descripcion=descripcion
    
    def setVisible(self,visible):
        self.visible=visible
    
    def getVisible(self):
        return self.visible

    def votarComentario(self):
        self.votos+=1
    
    def getvotos(self):
        return self.votos

