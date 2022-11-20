""" DiscussionEndpoints class module.
"""
from typing import Text, Union
from flask import redirect, request, flash, url_for, session, render_template
from werkzeug.wrappers import Response
from dms2223frontend.presentation.web.moderatorendpoints import reportes
from dms2223common.data import Role
from dms2223common.data.reportstatus import ReportStatus
from dms2223frontend.data.rest.authservice import AuthService
from .webauth import WebAuth
from dms2223common.data.Pregunta import Pregunta
from dms2223common.data.Respuesta import Respuesta
from dms2223common.data.Comentario import Comentario
from dms2223common.data.sentiment import Sentiment
from dms2223common.data.Reporte import Reporte

#TODO

preguntas = {
    0: Pregunta("Autor 1","Titulo 1","Descripcion 1"),
    1: Pregunta("Autor 2","Titulo 2","Descripcion 2"),
    2: Pregunta("Autor 3","Titulo 3","Descripcion 3")
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

    def vote_answers(auth_service: AuthService,id_pregunta: int, id_respuesta: int)-> Union[Response,Text]:
        if not WebAuth.test_token(auth_service):
            return redirect(url_for('get_login'))
        if Role.DISCUSSION.name not in session['roles']:
            return redirect(url_for('get_home'))

        name = session['user']

        pregunta = preguntas.get(id_pregunta)

        if pregunta is None:
            return redirect(url_for("get_discussion"))

        respuesta = pregunta.respuestas.get(id_respuesta)

        if respuesta is None:
            return redirect(url_for("get_question",id_pregunta=pregunta.id))
        if(name in respuesta.votantes):
            return redirect(url_for("get_question",id_pregunta=pregunta.id))
        
        respuesta.votantes.append(name)
        respuesta.votos+=1
        return redirect(url_for("get_question",id_pregunta=pregunta.id))

    def vote_comments(auth_service: AuthService,id_pregunta: int, id_respuesta: int, id_comentario: int)-> Union[Response,Text]:
        if not WebAuth.test_token(auth_service):
            return redirect(url_for('get_login'))
        if Role.DISCUSSION.name not in session['roles']:
            return redirect(url_for('get_home'))

        name = session['user']

        pregunta = preguntas.get(id_pregunta)

        if pregunta is None:
            return redirect(url_for("get_discussion"))

        respuesta = pregunta.respuestas.get(id_respuesta)

        if respuesta is None:
            return redirect(url_for("get_question",id_pregunta=pregunta.id))
        
        comentario= respuesta.comentarios.get(id_comentario)
        if comentario is None:
            return redirect(url_for("get_question",id_pregunta=pregunta.id))        
        if(name in comentario.votantes):
            return redirect(url_for("get_question",id_pregunta=pregunta.id))
        
        comentario.votantes.append(name)
        comentario.votos+=1
        return redirect(url_for("get_question",id_pregunta=pregunta.id))

    def report_answers(auth_service: AuthService,id_pregunta: int, id_respuesta: int)-> Union[Response,Text]:
        if not WebAuth.test_token(auth_service):
            return redirect(url_for('get_login'))
        if Role.DISCUSSION.name not in session['roles']:
            return redirect(url_for('get_home'))

        name = session['user']

        pregunta = preguntas.get(id_pregunta)

        if pregunta is None:
            return redirect(url_for("get_discussion"))

        respuesta = pregunta.respuestas.get(id_respuesta)

        if respuesta is None:
            return redirect(url_for("get_question",id_pregunta=pregunta.id))
        descripcion = request.form["descripcion"]

        if descripcion is None:
            return redirect(url_for("get_discussion"))
        reporte = Reporte(name,descripcion,respuesta,ReportStatus.PENDING)
        reportes[reporte.id] = reporte
        
        return redirect(url_for("get_question",id_pregunta=pregunta.id))

    def report_comments(auth_service: AuthService,id_pregunta: int, id_respuesta: int, id_comentario: int)-> Union[Response,Text]:
        if not WebAuth.test_token(auth_service):
            return redirect(url_for('get_login'))
        if Role.DISCUSSION.name not in session['roles']:
            return redirect(url_for('get_home'))

        name = session['user']

        pregunta = preguntas.get(id_pregunta)

        if pregunta is None:
            return redirect(url_for("get_discussion"))

        respuesta = pregunta.respuestas.get(id_respuesta)

        if respuesta is None:
            return redirect(url_for("get_question",id_pregunta=pregunta.id))
        
        comentario= respuesta.comentarios.get(id_comentario)
        if comentario is None:
            return redirect(url_for("get_question",id_pregunta=pregunta.id)) 
               
        descripcion = request.form["descripcion"]

        if descripcion is None:
            return redirect(url_for("get_discussion"))
        reporte = Reporte(name,descripcion,comentario,ReportStatus.PENDING)
        reportes[reporte.id] = reporte
        
        return redirect(url_for("get_question",id_pregunta=pregunta.id))

    def report_questions(auth_service: AuthService,id_pregunta: int)-> Union[Response,Text]:
        if not WebAuth.test_token(auth_service):
            return redirect(url_for('get_login'))
        if Role.DISCUSSION.name not in session['roles']:
            return redirect(url_for('get_home'))

        name = session['user']

        pregunta = preguntas.get(id_pregunta)

        if pregunta is None:
            return redirect(url_for("get_discussion"))
               
        descripcion = request.form["descripcion"]

        if descripcion is None:
            return redirect(url_for("get_discussion"))
        reporte = Reporte(descripcion,name,pregunta,ReportStatus.PENDING)

        reportes[reporte.id] = reporte

        return redirect(url_for("get_question",id_pregunta=pregunta.id))