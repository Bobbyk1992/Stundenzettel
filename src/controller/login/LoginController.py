from .. import Controller
from flask import render_template, request, redirect, url_for, session
"""from ...packages.login import Login"""

class LoginController(Controller):

    def __init__(self):
        self.superusers = []
        self.stations = []

    def get_login_form(self):
        response = False

        return render_template('login/login.html', fehler=response)