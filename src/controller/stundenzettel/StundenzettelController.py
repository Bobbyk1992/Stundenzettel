from src.controller.Controller import Controller
from src.controller.database.DatabaseController import DatabaseController
from src.packages.stundenzettel.Stundenzettel import Stundenzettel
from flask import render_template, request, redirect, url_for, session

class StundenzettelController(Controller):

    def __init__(self):
        pass

    def get_stundenzettel_form(self):

        information = ' '

        db = DatabaseController()
        st = Stundenzettel()
        kalenderwoche = db.get_selected_information('datepart(wk, GETDATE()) AS Kalenderwoche')


        if request.method == 'POST':


            information = st.validate_stundenzettel_date()
            kalenderwoche = st.get_kalenderwoche_stundenzettel()

            cursor = db.get_many_information('Stundenzettel', 'BearbeiterID = ' + str(session['Personalnummer']) + information)

        cursor = db.get_selected_information('*', 'Stundenzettel', 'Datepart(wk,Datum) = DATEPART(wk, (Select MAX(Datum) As Datum From Stundenzettel Where Freigabe is Null or Freigabe = 0 And BearbeiterID = ' + str(session['Personalnummer']) + ' ))')
        persocursor = db.get_many_information('Mitarbeiter', 'Personalnummer = ' + str(session['Personalnummer']))
        montag = st.wochentag_summe(1)
        dienstag = st.wochentag_summe(2)
        mittwoch = st.wochentag_summe(3)
        donnerstag = st.wochentag_summe(4)
        freitag = st.wochentag_summe(5)
        samstag = st.wochentag_summe(6)
        sonntag = st.wochentag_summe(7)
        weekday = [montag, dienstag, mittwoch, donnerstag, freitag, samstag, sonntag]
        x = 0
        return render_template('stundenzettel/stundenzettel.html', daten=cursor , x=x, success=request.args.get('success'), day= weekday, personal=persocursor, kw=kalenderwoche)