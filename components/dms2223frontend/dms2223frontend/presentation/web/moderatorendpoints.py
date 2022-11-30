""" ModeratorEndpoints class module.
"""

from typing import Dict, Text, Union
from flask import redirect, url_for, session, render_template, request
from werkzeug.wrappers import Response
from dms2223common.data import Role
from dms2223frontend.data.rest.authservice import AuthService
from .webauth import WebAuth
from dms2223common.data.reportstatus import ReportStatus
from dms2223common.data.Reporte import Reporte

reportes: Dict[int,Reporte] = {}
class ModeratorEndpoints():
    """ Monostate class responsible of handing the moderator web endpoint requests.
    """
    @staticmethod
    def get_moderator(auth_service: AuthService) -> Union[Response, Text]:
        """ Handles the GET requests to the moderator root endpoint.

        Args:
            - auth_service (AuthService): The authentication service.

        Returns:
            - Union[Response,Text]: The generated response to the request.
        """
        if not WebAuth.test_token(auth_service):
            return redirect(url_for('get_login'))
        if Role.MODERATION.name not in session['roles']:
            return redirect(url_for('get_home'))
        name:str = session['user']
        return render_template('moderator.html', name=name, roles=session['roles'],reportes=reportes)

    @staticmethod
    def get_report(auth_service: AuthService, id_reporte: int) -> Union[Response, Text]:

        if not WebAuth.test_token(auth_service):
            return redirect(url_for('get_login'))
        if Role.MODERATION.name not in session['roles']:
            return redirect(url_for('get_home'))

        name:str = session['user']

        reporte = reportes.get(id_reporte)

        if reporte is None or reporte.getEstado() != 1:
            return redirect(url_for("get_moderator"))

        return render_template('report.html', name=name, roles=session['roles'], reporte=reporte)

    @staticmethod
    def post_report(auth_service: AuthService,id_reporte: int):
        if not WebAuth.test_token(auth_service):
            return redirect(url_for('get_login'))
        if Role.MODERATION.name not in session['roles']:
            return redirect(url_for('get_home'))

        
        reporte = reportes.get(id_reporte)

        if reporte is None:
            return redirect(url_for("get_moderator"))
        
        if request.form["opcion"] == "aceptar":
            if reporte.getElemento() is not None:
                reporte.getElemento().cambiarVisible()
            reporte.setEstado(ReportStatus.ACCEPTED)
        elif request.form["opcion"] == "rechazar":
            reporte.setEstado(ReportStatus.REJECTED)

        return redirect(url_for("get_moderator"))