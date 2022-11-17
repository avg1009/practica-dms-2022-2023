from datetime import datetime

class Respuesta :
    def __init__(self, autor, respuesta):
        self.autor = autor
        self.fechaRespuesta = datetime.now()
        self.respuesta = respuesta
        self.visible = True
        self.votos = 0

    # votar respuesta
    def votarRespuesta(self):
        self.votos += 1

    # reportar respuesta
    def reportarRespuesta(self):
        pass

    # visibilidad respuesta
    def cambiarVisibilidad(self):
        self.visible = not self.visible