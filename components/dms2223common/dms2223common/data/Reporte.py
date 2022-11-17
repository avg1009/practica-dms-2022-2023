import string
import datetime


class Reporte:

    def __init__(self, descripcion,autor,elemento):
        self.descripcion: string = descripcion
        self.autor= autor
        self.fechaReporte = datetime.now()
        self.elemento= elemento
        

    def getDescripcion(self):
        return self.descripcion

    def setDescripcion(self,descripcion):
        self.descripcion=descripcion
    
    def setAutor(self,autor):
        self.autor=autor
    
    def getAutor(self):
        return self.autor
    
    def setElemento(self,elemento):
        self.elemento=elemento
    
    def getElemento(self):
        return self.elemento
    
    def getFechaReporte(self):
        return self.fechaReporte