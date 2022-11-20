""" DiscussionEndpoints class module.
"""
from typing import Text, Union
from flask import redirect, request, flash, url_for, session, render_template
from werkzeug.wrappers import Response
from dms2223common.data import Role
from dms2223frontend.data.rest.authservice import AuthService
from .webauth import WebAuth
from dms2223common.data.Pregunta import Pregunta
from dms2223common.data.Respuesta import Respuesta
from dms2223common.data.Comentario import Comentario
from dms2223common.data.Reporte import Reporte
from dms2223common.data.sentiment import Sentiment

#TODO

preguntas = {
    0: Pregunta("Autor 1","Titulo 1","Descripcion 1"),
    1: Pregunta("Autor 2","Titulo 2","Descripcion 2"),
    2: Pregunta("Autor 3","Titulo 3","Descripcion 3")
}

respuestas = {
    0: Respuesta("Autor 1", "Respuesta 1", preguntas[0]),
    1: Respuesta("Autor 2","Respuesta 2", preguntas[1]),
    2: Respuesta("Autor 3", "Respuesta 3", preguntas[2])
}

comentarios = {
    0: Comentario("Autor 1","Descripcion 1", respuestas[0],Sentiment.NEUTRAL),
    1: Comentario("Autor 2","Descripcion 2", respuestas[1],Sentiment.NEUTRAL),
    2: Comentario("Autor 3","Descripcion 3", respuestas[2],Sentiment.NEUTRAL)
}

reportes = {
    0: Reporte("Descripcion 1", "Autor 1", preguntas[0], 1),
    1: Reporte("Descripcion 2", "Autor 2", respuestas[0], 1),
    2: Reporte("Descripcion 3", "Autor 3", comentarios[0], 1),
}

class DiscussionEndpoints():
    """ Monostate class responsible of handling the discussion web endpoint requests.
    """
    @staticmethod
    def get_discussion(auth_service: AuthService) -> Union[Response, Text]:
        """ Handles the GET requests to the discussion root endpoint.

        Args:
            - auth_service (AuthService): The authentication service.

        Returns:
            - Union[Response,Text]: The generated response to the request.
        """
        if not WebAuth.test_token(auth_service):
            return redirect(url_for('get_login'))
        if Role.DISCUSSION.name not in session['roles']:
            return redirect(url_for('get_home'))
        name = session['user']
        
        return render_template('discussion.html', name=name, roles=session['roles'], preguntas=preguntas)

    @staticmethod
    def post_discussion(auth_service: AuthService) -> Union[Response,Text]:


        if not WebAuth.test_token(auth_service):
            return redirect(url_for('get_login'))
        if Role.DISCUSSION.name not in session['roles']:
            return redirect(url_for('get_home'))
        name = session['user']
        

        if request.form['titulo'] == "" or request.form['descripcion'] == "":
            flash('Introduce pregunta', 'error')
            return redirect(url_for('get_discussion'))
        
        pregunta: Pregunta = Pregunta(session['user'],request.form['titulo'],request.form['descripcion'])
        preguntas[pregunta.getId()]=pregunta
        return render_template('discussion.html', name=name, roles=session['roles'], preguntas=preguntas)

    
    @staticmethod
    def get_question(auth_service: AuthService, id_pregunta: int) -> Union[Response, Text]:
        """ Handles the GET requests to the discussion root endpoint.

        Args:
            - auth_service (AuthService): The authentication service.

        Returns:
            - Union[Response,Text]: The generated response to the request.
        """
        if not WebAuth.test_token(auth_service):
            return redirect(url_for('get_login'))
        if Role.DISCUSSION.name not in session['roles']:
            return redirect(url_for('get_home'))

        name = session['user']

        pregunta = preguntas.get(id_pregunta)

        if pregunta is None:
            redirect(url_for("get_discussion"))

        return render_template('question.html', name=name, roles=session['roles'], pregunta=pregunta)

    @staticmethod
    def post_question(auth_service: AuthService,id_pregunta: int) -> Union[Response,Text]:


        if not WebAuth.test_token(auth_service):
            return redirect(url_for('get_login'))
        if Role.DISCUSSION.name not in session['roles']:
            return redirect(url_for('get_home'))

        name = session['user']


        pregunta = preguntas.get(id_pregunta)
        if pregunta is None:
            return redirect(url_for("get_discussion"))

        if request.form['descripcion'] == "":
            flash('Introduce respuesta', 'error')
        else:
            pregunta.addRespuesta(Respuesta(session['user'],request.form['descripcion'],pregunta))
        
        return redirect(url_for("get_question",id_pregunta=pregunta.id))


    @staticmethod
    def post_comment(auth_service: AuthService,id_pregunta: int,id_respuesta: int) -> Union[Response,Text]:


        if not WebAuth.test_token(auth_service):
            return redirect(url_for('get_login'))
        if Role.DISCUSSION.name not in session['roles']:
            return redirect(url_for('get_home'))

        name = session['user']

        pregunta = preguntas.get(id_pregunta)

        if pregunta is None:
            return redirect(url_for("get_discussion"))

        respuesta = pregunta.respuestas.get(id_respuesta)

        if request.form['descripcion'] != "" and request.form['sentimiento'] != "":
            respuesta.addComentario(Comentario(session['user'],request.form['descripcion'],respuesta,int(request.form['sentimiento'])))
        
        return redirect(url_for("get_question",id_pregunta=pregunta.id))
   
