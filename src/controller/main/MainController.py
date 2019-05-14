from flask import render_template
from ..Controller import Controller


class MainController(Controller):
    def __init__(self):
        pass

    def index(self):
        """Diese Funktion gibt die Hauptseite aus"""
        return render_template('main/index.html')
