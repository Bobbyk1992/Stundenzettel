from src.packages.login.abstract.AbstractLogin import AbstractLogin
from src.controller.database.DatabaseController import DatabaseController
from flask import session, request, url_for

class Login(AbstractLogin):

    def __init__(self):
        super().__init__()

        self.user = []

    def get_login_information(self):
        db = DatabaseController()

        self.user = db.get_one_information()

    def validate_login_request(self):
        information = None
        self.get_login_information()

        for personal in self.user:
            if request.form['login-username'] == personal['Personalnummer'] and request.form['login-password'] == personal['Password']:
                information = {'role': 'user', 'route': 'stundenzettel', 'redirect': 'stundenzettel'}

        return information

    def login(self, information):
        session['Personalnummer'] = request.form['login-username']
        session['role'] = information['role']
        session['defaultRoute'] = information['route']

    def logout(self):
        session.pop('Personalnummer', None)
        session.pop('role', None)
        session.pop('defaultRoute', None)
