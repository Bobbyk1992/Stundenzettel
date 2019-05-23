from flask import Flask, session , redirect, url_for, request, render_template

from src.controller.main.MainController import MainController
from src.controller.error.ErrorController import ErrorController
from src.controller.login.LoginController import LoginController
from src.controller.stundenzettel.StundenzettelController import StundenzettelController


app = Flask(__name__)
app.secret_key = b'_87fgT%6#8jsd32\n\xec]/'

@app.route('/')
def index():
    obj = MainController()
    return obj.index()

@app.route('/stundenzettel', methods=['GET', 'POST'])
def stundenzettel_form():

    if 'role' not in session or session['role'] != 'user':
        return redirect(url_for('login_form'))

    obj = StundenzettelController()
    return obj.get_stundenzettel_form()
    """return render_template('stundenzettel/stundenzettel.html', success=request.args.get('success'))"""

@app.route('/login', methods=['GET', 'POST'])
def login_form():
    if 'role' not in session:
        obj = LoginController()
        return obj.get_login_form()

    return redirect(url_for(session['defaultRoute']))

@app.route('/logout')
def logout():
    obj = LoginController()
    return obj.logout()

@app.errorhandler(400)
def internal_error(error):
    obj = ErrorController()
    return obj.get_error_template(error, 400)


@app.errorhandler(403)
def internal_error(error):
    obj = ErrorController()
    return obj.get_error_template(error, 403)


@app.errorhandler(404)
def not_found(error):
    obj = ErrorController()
    return obj.get_error_template(error, 404)


@app.errorhandler(405)
def not_allowed(error):
    obj = ErrorController()
    return obj.get_error_template(error, 405)


@app.errorhandler(406)
def internal_error(error):
    obj = ErrorController()
    return obj.get_error_template(error, 406)


@app.errorhandler(500)
def internal_error(error):
    obj = ErrorController()
    return obj.get_error_template(error, 500)


@app.errorhandler(502)
def internal_error(error):
    obj = ErrorController()
    return obj.get_error_template(error, 502)


@app.errorhandler(503)
def internal_error(error):
    obj = ErrorController()
    return obj.get_error_template(error, 503)


if __name__ == '__main__':
    app.run()
