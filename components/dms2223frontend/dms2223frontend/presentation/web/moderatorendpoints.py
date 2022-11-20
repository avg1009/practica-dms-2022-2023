""" ModeratorEndpoints class module.
"""

from typing import Text, Union
from flask import redirect, url_for, session, render_template
from werkzeug.wrappers import Response
from dms2223common.data import Role
from dms2223frontend.data.rest.authservice import AuthService
from .webauth import WebAuth
from dms2223common.data.Reporte import Reporte
from dms2223frontend.dms2223frontend.presentation.web.discussionendpoints import preguntas
from dms2223frontend.dms2223frontend.presentation.web.discussionendpoints import respuestas
from dms2223frontend.dms2223frontend.presentation.web.discussionendpoints import comentarios

reportes = {
    0: Reporte("Descripcion 1", "Autor 1", preguntas[0], 1),
    1: Reporte("Descripcion 2", "Autor 2", respuestas[0], 1),
    2: Reporte("Descripcion 3", "Autor 3", comentarios[0], 1),
}
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
        name = session['user']
        return render_template('moderator.html', name=name, roles=session['roles'])

    @staticmethod
    def get_report(auth_service: AuthService, id_reporte: int) -> Union[Response, Text]:

        if not WebAuth.test_token(auth_service):
            return redirect(url_for('get_login'))
        if Role.MODERATION.name not in session['roles']:
            return redirect(url_for('get_home'))

        name = session['user']

        reporte = reportes.get(id_reporte)

        if reporte is None:
            redirect(url_for("get_moderator"))

        return render_template('report.html', name=name, roles=session['roles'], reporte=reporte)

