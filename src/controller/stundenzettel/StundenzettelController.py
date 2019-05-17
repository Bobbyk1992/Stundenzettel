from .. import Controller
from flask import render_template, request, redirect, url_for, session

class StundenzettelController(Controller):

    def __init__(self):
        pass

    def get_stundenzettel_form(self):

        return render_template('stundenzettel/stundenzettel.html')