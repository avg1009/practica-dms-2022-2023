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

#TODO

preguntas= [
    Pregunta("Autor 1","Titulo 1","Descripcion 1"),
    Pregunta("Autor 2","Titulo 2","Descripcion 2"),
    Pregunta("Autor 3","Titulo 3","Descripcion 3")
]

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
        
        preguntas.append(Pregunta(session['user'],request.form['titulo'],request.form['descripcion']))
        return render_template('discussion.html', name=name, roles=session['roles'], preguntas=preguntas)

    
    @staticmethod
    def get_answers(auth_service: AuthService) -> Union[Response, Text]:
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
        titulo = str(request.args.get('titulo'))

        pregunta: Pregunta
        for preguntaAux in preguntas:
            if preguntaAux.titulo == titulo:
                pregunta = preguntaAux
                break
        return render_template('answers.html', name=name, roles=session['roles'], pregunta=pregunta)


    @staticmethod
    def post_answers(auth_service: AuthService) -> Union[Response,Text]:


        if not WebAuth.test_token(auth_service):
            return redirect(url_for('get_login'))
        if Role.DISCUSSION.name not in session['roles']:
            return redirect(url_for('get_home'))

        name = session['user']
        titulo = str(request.args.get('titulo'))

        pregunta: Pregunta
        for preguntaAux in preguntas:
            if preguntaAux.titulo == titulo:
                pregunta = preguntaAux
                break       

        if request.form['titulo'] == "" or request.form['descripcion'] == "":
            flash('Introduce pregunta', 'error')
            return redirect(url_for('get_answer'))
        
        pregunta.addRespuesta(Respuesta(session['user'],request.form['descripcion']))
        return render_template('answers.html', name=name, roles=session['roles'], pregunta=pregunta)

    @staticmethod
    def get_comment(auth_service: AuthService) -> Union[Response, Text]:
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
        pregunta = session['pregunta']
        answer = session['answer']
        
        return render_template('answer.html', name=name, roles=session['roles'], pregunta=pregunta, answer=answer)


    @staticmethod
    def post_comment(auth_service: AuthService) -> Union[Response,Text]:


        if not WebAuth.test_token(auth_service):
            return redirect(url_for('get_login'))
        if Role.DISCUSSION.name not in session['roles']:
            return redirect(url_for('get_home'))

        name = session['user']
        pregunta = session['pregunta']        
        answer = session['answer']

        if request.form['titulo'] == "" or request.form['descripcion'] == "":
            flash('Introduce pregunta', 'error')
            return redirect(url_for('get_answer'))
        
        answer.crearComentario(Comentario(session['user'],request.form['descripcion']))
        return render_template('answer.html', name=name, roles=session['roles'], pregunta=pregunta)