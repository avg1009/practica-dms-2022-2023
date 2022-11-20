import string
import datetime
import itertools

from dms2223common.data import reportstatus

class Reporte:

    id_iter=itertools.count()

    def __init__(self, descripcion, autor, elemento, estado):
        self.id=next(Reporte.id_iter)
        self.descripcion: string = descripcion
        self.autor= autor
        self.fechaReporte = datetime.now()
        self.elemento = elemento
        self.estado: reportstatus = estado
        
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
    
    def getId(self):
        return self.id

    def setEstado(self,estado):
        self.estado=estado
    
    def getEstado(self):
        return self.estado