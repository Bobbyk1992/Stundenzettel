from src.packages.stundenzettel.abstract.AbstractStundenzettel import AbstractStundenzettel
from src.controller.database.DatabaseController import DatabaseController
from flask import session, request, url_for
from datetime import datetime

class Stundenzettel(AbstractStundenzettel):

    def __init__(self):
        super().__init__()

    def wochentag_summe(self, wochentag):

        db = DatabaseController()

        if wochentag == 1:
            return db.get_selected_information('SUM(Stunden) As SummeStd','Stundenzettel', 'DATEPART(dw,Datum) = 1')

        elif wochentag == 2:
            return db.get_selected_information('SUM(Stunden) As SummeStd','Stundenzettel', 'DATEPART(dw,Datum) = 2')

        elif wochentag == 3:
            return db.get_selected_information('SUM(Stunden) As SummeStd','Stundenzettel', 'DATEPART(dw,Datum) = 3')

        elif wochentag == 4:
            return db.get_selected_information('SUM(Stunden) As SummeStd','Stundenzettel', 'DATEPART(dw,Datum) = 4')

        elif wochentag == 5:
            return db.get_selected_information('SUM(Stunden) As SummeStd','Stundenzettel', 'DATEPART(dw,Datum) = 5')

        elif wochentag == 6:
            return db.get_selected_information('SUM(Stunden) As SummeStd','Stundenzettel', 'DATEPART(dw,Datum) = 6')

        elif wochentag == 7:
            return db.get_selected_information('SUM(Stunden) As SummeStd','Stundenzettel', 'DATEPART(dw,Datum) = 7')

        else:
            print('Es gibt nur 7 Wochentage z.B. 1 = Montag ...')



    def validate_stundenzettel_date(self):

        db = DatabaseController()

        vonDatum = request.form['vonDatum']
        bisDatum = request.form['bisDatum']

        if vonDatum == None or bisDatum == None:

            vonDatum = ' '
            bisDatum = ' '

        info = 'between ' + vonDatum + ' And ' + bisDatum
        info = str(info)
        return info