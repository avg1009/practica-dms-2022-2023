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
    def get_question(auth_service: AuthService) -> Union[Response, Text]:
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
        id_p = int(request.args.get('id_p'))

        pregunta: Pregunta
        for preguntaAux in preguntas:
            if preguntaAux.id== id_p:
                pregunta = preguntaAux
                break

        return render_template('question.html', name=name, roles=session['roles'], pregunta=pregunta)

    @staticmethod
    def post_question(auth_service: AuthService) -> Union[Response,Text]:


        if not WebAuth.test_token(auth_service):
            return redirect(url_for('get_login'))
        if Role.DISCUSSION.name not in session['roles']:
            return redirect(url_for('get_home'))

        name = session['user']
        tipo = request.form.get('tipo')
        id_p = int(request.form.get('id_pregunta'))


        pregunta: Pregunta
        for preguntaAux in preguntas:
            if preguntaAux.id== id_p:
                pregunta = preguntaAux
                break

        if (tipo == "respuesta") :
            if request.form['descripcion'] == "":
                flash('Introduce respuesta', 'error')
            else:
                pregunta.addRespuesta(Respuesta(session['user'],request.form['descripcion'],pregunta))
        elif (tipo == "comentario"):   
            id_r = int(request.form.get('id_respuesta'))
            respuesta: Respuesta
            for respuestaAux in pregunta.getRespuestas():
                if respuestaAux.id== id_r:
                    respuesta = respuestaAux
                    break
            if request.form['descripcion'] == "" or request.form['sentimiento'] == "":
                flash('Introduce comentario', 'error')
            else:
                respuesta.addComentario(Comentario(session['user'],request.form['descripcion'],respuesta,int(request.form['sentimiento'])))
        
        return render_template('question.html', name=name, roles=session['roles'], pregunta=pregunta)


    '''
    @staticmethod
    def post_answer(auth_service: AuthService) -> Union[Response,Text]:


        if not WebAuth.test_token(auth_service):
            return redirect(url_for('get_login'))
        if Role.DISCUSSION.name not in session['roles']:
            return redirect(url_for('get_home'))

        name = session['user']
        id_p = int(request.form.get('id_pregunta'))

        pregunta: Pregunta
        for preguntaAux in preguntas:
            if preguntaAux.id== id_p:
                pregunta = preguntaAux
                break     

        if request.form['descripcion'] == "":
            flash('Introduce respuesta', 'error')
            return redirect(url_for('get_answer'))
        
        pregunta.addRespuesta(Respuesta(session['user'],request.form['descripcion'],pregunta))
        return render_template('question.html', name=name, roles=session['roles'], pregunta=pregunta)

    @staticmethod
    def post_comment(auth_service: AuthService) -> Union[Response,Text]:


        if not WebAuth.test_token(auth_service):
            return redirect(url_for('get_login'))
        if Role.DISCUSSION.name not in session['roles']:
            return redirect(url_for('get_home'))

        name = session['user']
        id_p = int(request.form.get('id_pregunta'))
        id_r = int(request.form.get('id_respuesta'))

        pregunta: Pregunta
        for preguntaAux in preguntas:
            if preguntaAux.id== id_p:
                pregunta = preguntaAux
                break

        respuesta: Respuesta
        for respuestaAux in pregunta.getRespuestas():
            if respuestaAux.id== id_r:
                respuesta = respuestaAux
                break

        if request.form['descripcion'] != "" and request.form['sentimiento'] != "":
            respuesta.addComentario(Comentario(session['user'],request.form['descripcion'],respuesta,int(request.form['sentimiento'])))
        
        return render_template('question.html', name=name, roles=session['roles'], pregunta=pregunta)
    '''
   
