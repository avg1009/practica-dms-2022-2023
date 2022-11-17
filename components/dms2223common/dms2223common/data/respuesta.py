from datetime import datetime

class Respuesta :
    def __init__(self, autor, respuesta):
        self.autor = autor
        self.fechaRespuesta = datetime.now()
        self.respuesta = respuesta
        self.visible = True
        self.votos = 0
        self.comentarios = list()

    # votar respuesta
    def votarRespuesta(self):
        self.votos += 1

    # reportar respuesta
    def reportarRespuesta(self):
        pass

    # visibilidad respuesta
    def cambiarVisibilidad(self):
        self.visible = not self.visible

    #crear comentario
    def crearComentario(self, comentario):
        self.comentarios.append(comentario)