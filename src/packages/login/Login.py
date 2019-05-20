from flask import session, request, url_for
from ...controller.database import DatabaseController
from .abstract.AbstractLogin import AbstractLogin

class Login(AbstractLogin):

    def __init__(self):
        super().__init__()

    def get_login_information(self):
        db = DatabaseController()

        self.user = db.get_information()