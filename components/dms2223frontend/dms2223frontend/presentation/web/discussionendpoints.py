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
    1: Pregunta("Autor 1","Titulo 1","Descripcion 1",1),
    2: Pregunta("Autor 2","Titulo 2","Descripcion 2",2),
    3: Pregunta("Autor 3","Titulo 3","Descripcion 3",3)
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
        
        pregunta: Pregunta = Pregunta(session['user'],request.form['titulo'],request.form['descripcion'],0)
        id = pregunta.getId()
        if id is None:
            return redirect(url_for('get_discussion'))
        preguntas[id]=pregunta
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

        name:str = session['user']
        
        pregunta = preguntas.get(id_pregunta)

        if pregunta is None or not pregunta.getVisible():
            return redirect(url_for("get_discussion"))

        return render_template('question.html', name=name, roles=session['roles'], pregunta=pregunta)

    @staticmethod
    def post_answer(auth_service: AuthService,id_pregunta: int) -> Union[Response,Text]:


        if not WebAuth.test_token(auth_service):
            return redirect(url_for('get_login'))
        if Role.DISCUSSION.name not in session['roles']:
            return redirect(url_for('get_home'))

        pregunta = preguntas.get(id_pregunta)
        if pregunta is None:
            return redirect(url_for("get_discussion"))

        if request.form['descripcion'] == "":
            flash('Introduce respuesta', 'error')
        else:
            pregunta.addRespuesta(Respuesta(session['user'],request.form['descripcion'],0))
        
        return redirect(url_for("get_question",id_pregunta=pregunta.getId()))


    @staticmethod
    def post_comment(auth_service: AuthService,id_pregunta: int,id_respuesta: int) -> Union[Response,Text]:


        if not WebAuth.test_token(auth_service):
            return redirect(url_for('get_login'))
        if Role.DISCUSSION.name not in session['roles']:
            return redirect(url_for('get_home'))

        pregunta = preguntas.get(id_pregunta)

        if pregunta is None:
            return redirect(url_for("get_discussion"))

        respuesta = pregunta.getRespuestas().get(id_respuesta)

        if request.form['descripcion'] != "" and request.form['sentimiento'] != "" and respuesta is not None:
            sentiment = next((x for x in Sentiment if x == int(request.form['sentimiento'])))
            respuesta.addComentario(Comentario(session['user'],request.form['descripcion'], sentiment ,0))
        
        return redirect(url_for("get_question",id_pregunta=pregunta.getId()))

    @staticmethod
    def vote_answers(auth_service: AuthService,id_pregunta: int, id_respuesta: int)-> Union[Response,Text]:
        if not WebAuth.test_token(auth_service):
            return redirect(url_for('get_login'))
        if Role.DISCUSSION.name not in session['roles']:
            return redirect(url_for('get_home'))

        name:str = session['user']

        pregunta = preguntas.get(id_pregunta)

        if pregunta is None:
            return redirect(url_for("get_discussion"))

        respuesta = pregunta.getRespuestas().get(id_respuesta)

        if respuesta is None:
            return redirect(url_for("get_question",id_pregunta=pregunta.getId()))
        if(name in respuesta.getVotantes()):
            return redirect(url_for("get_question",id_pregunta=pregunta.getId()))
        
        respuesta.addVotantes(name)
        respuesta.votar()
        return redirect(url_for("get_question",id_pregunta=pregunta.getId()))

    @staticmethod
    def vote_comments(auth_service: AuthService,id_pregunta: int, id_respuesta: int, id_comentario: int)-> Union[Response,Text]:
        if not WebAuth.test_token(auth_service):
            return redirect(url_for('get_login'))
        if Role.DISCUSSION.name not in session['roles']:
            return redirect(url_for('get_home'))

        name:str = session['user']

        pregunta = preguntas.get(id_pregunta)

        if pregunta is None:
            return redirect(url_for("get_discussion"))

        respuesta = pregunta.getRespuestas().get(id_respuesta)

        if respuesta is None:
            return redirect(url_for("get_question",id_pregunta=pregunta.getId()))
        
        comentario= respuesta.getComentarios().get(id_comentario)
        if comentario is None:
            return redirect(url_for("get_question",id_pregunta=pregunta.getId()))        
        if(name in comentario.getVotantes()):
            return redirect(url_for("get_question",id_pregunta=pregunta.getId()))
        
        comentario.addVotantes(name)
        comentario.votar()
        return redirect(url_for("get_question",id_pregunta=pregunta.getId()))

    @staticmethod
    def report_answers(auth_service: AuthService,id_pregunta: int, id_respuesta: int)-> Union[Response,Text]:
        if not WebAuth.test_token(auth_service):
            return redirect(url_for('get_login'))
        if Role.DISCUSSION.name not in session['roles']:
            return redirect(url_for('get_home'))

        name:str = session['user']

        pregunta = preguntas.get(id_pregunta)

        if pregunta is None:
            return redirect(url_for("get_discussion"))

        respuesta = pregunta.getRespuestas().get(id_respuesta)

        if respuesta is None:
            return redirect(url_for("get_question",id_pregunta=pregunta.getId()))
        descripcion = request.form["descripcion"]

        if descripcion is None:
            return redirect(url_for("get_discussion"))
        reporte = Reporte(descripcion,name,respuesta,ReportStatus.PENDING,0)
        id = reporte.getId()
        if id is not None:
            reportes[id] = reporte
        
        return redirect(url_for("get_question",id_pregunta=pregunta.getId()))

    @staticmethod
    def report_comments(auth_service: AuthService,id_pregunta: int, id_respuesta: int, id_comentario: int)-> Union[Response,Text]:
        if not WebAuth.test_token(auth_service):
            return redirect(url_for('get_login'))
        if Role.DISCUSSION.name not in session['roles']:
            return redirect(url_for('get_home'))

        name:str = session['user']

        pregunta = preguntas.get(id_pregunta)

        if pregunta is None:
            return redirect(url_for("get_discussion"))

        respuesta = pregunta.getRespuestas().get(id_respuesta)

        if respuesta is None:
            return redirect(url_for("get_question",id_pregunta=pregunta.getId()))
        
        comentario= respuesta.getComentarios().get(id_comentario)
        if comentario is None:
            return redirect(url_for("get_question",id_pregunta=pregunta.getId())) 
               
        descripcion = request.form["descripcion"]

        if descripcion is None:
            return redirect(url_for("get_discussion"))
        reporte = Reporte(descripcion,name,comentario,ReportStatus.PENDING,0)
        id = reporte.getId()
        if id is not None:
            reportes[id] = reporte
        
        return redirect(url_for("get_question",id_pregunta=pregunta.getId()))

    @staticmethod
    def report_questions(auth_service: AuthService,id_pregunta: int)-> Union[Response,Text]:
        if not WebAuth.test_token(auth_service):
            return redirect(url_for('get_login'))
        if Role.DISCUSSION.name not in session['roles']:
            return redirect(url_for('get_home'))

        name:str = session['user']

        pregunta = preguntas.get(id_pregunta)

        if pregunta is None:
            return redirect(url_for("get_discussion"))
               
        descripcion = request.form["descripcion"]

        if descripcion is None:
            return redirect(url_for("get_discussion"))
        reporte = Reporte(descripcion,name,pregunta,ReportStatus.PENDING,0)

        id = reporte.getId()
        if id is not None:
            reportes[id] = reporte

        return redirect(url_for("get_question",id_pregunta=pregunta.getId()))