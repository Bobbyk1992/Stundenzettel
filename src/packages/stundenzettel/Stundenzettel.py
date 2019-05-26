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
            return db.get_selected_information('SUM(Stunden) As SummeStd','Stundenzettel', 'DATEPART(dw,Datum) = 1 And ' +
                                                                                           'Datepart(wk,Datum) = '
                                                                                           'DATEPART(wk, (Select MAX(Datum) As Datum '
                                                                                                         'From Stundenzettel '
                                                                                                         'Where Freigabe is Null or Freigabe = 0 And BearbeiterID = '
                                                                                                         + str(session['Personalnummer']) + ' ))' +
                                                                                           'And DATEPART(YYYY, Datum) = ' 
                                                                                           'DATEPART(YYYY, (Select MAX(Datum) As Datum '
                                                                                                        'From Stundenzettel '
                                                                                                        'Where Freigabe is Null or Freigabe = 0 And BearbeiterID = '
                                                                                                         + str(session['Personalnummer']) + ' ))' )

        elif wochentag == 2:
            return db.get_selected_information('SUM(Stunden) As SummeStd','Stundenzettel', 'DATEPART(dw,Datum) = 2 And ' +
                                                                                           'Datepart(wk,Datum) = '
                                                                                           'DATEPART(wk, (Select MAX(Datum) As Datum '
                                                                                                         'From Stundenzettel '
                                                                                                         'Where Freigabe is Null or Freigabe = 0 And BearbeiterID = '
                                                                                                         + str(session['Personalnummer']) + ' ))' 
                                                                                           'And DATEPART(YYYY, Datum) = '
                                                                                           'DATEPART(YYYY, (Select MAX(Datum) As Datum '
                                                                                                         'From Stundenzettel '
                                                                                                         'Where Freigabe is Null or Freigabe = 0 And BearbeiterID = '
                                                                                                         + str(session['Personalnummer']) + ' ))' )
        elif wochentag == 3:
            return db.get_selected_information('SUM(Stunden) As SummeStd','Stundenzettel', 'DATEPART(dw,Datum) = 3 And ' +
                                                                                           'Datepart(wk,Datum) = '
                                                                                           'DATEPART(wk, (Select MAX(Datum) As Datum '
                                                                                                         'From Stundenzettel '
                                                                                                         'Where Freigabe is Null or Freigabe = 0 And BearbeiterID = '
                                                                                                         + str(session['Personalnummer']) + ' ))'
                                                                                           'And DATEPART(YYYY, Datum) = '
                                                                                           'DATEPART(YYYY, (Select MAX(Datum) As Datum '
                                                                                                         'From Stundenzettel '
                                                                                                         'Where Freigabe is Null or Freigabe = 0 And BearbeiterID = '
                                                                                                         + str(session['Personalnummer']) + ' ))')

        elif wochentag == 4:
            return db.get_selected_information('SUM(Stunden) As SummeStd','Stundenzettel', 'DATEPART(dw,Datum) = 4 And ' +
                                                                                           'Datepart(wk,Datum) = '
                                                                                           'DATEPART(wk, (Select MAX(Datum) As Datum '
                                                                                                         'From Stundenzettel '
                                                                                                         'Where Freigabe is Null or Freigabe = 0 And BearbeiterID = '
                                                                                                         + str(session['Personalnummer']) + ' ))'
                                                                                           'And DATEPART(YYYY, Datum) = '
                                                                                           'DATEPART(YYYY, (Select MAX(Datum) As Datum '
                                                                                                         'From Stundenzettel '
                                                                                                         'Where Freigabe is Null or Freigabe = 0 And BearbeiterID = '
                                                                                                         + str(session['Personalnummer']) + ' ))')

        elif wochentag == 5:
            return db.get_selected_information('SUM(Stunden) As SummeStd','Stundenzettel', 'DATEPART(dw,Datum) = 5 And ' +
                                                                                           'Datepart(wk,Datum) = '
                                                                                           'DATEPART(wk, (Select MAX(Datum) As Datum '
                                                                                                         'From Stundenzettel '
                                                                                                         'Where Freigabe is Null or Freigabe = 0 And BearbeiterID = '
                                                                                                         + str(session['Personalnummer']) + ' ))'
                                                                                           'And DATEPART(YYYY, Datum) = '
                                                                                           'DATEPART(YYYY, (Select MAX(Datum) As Datum '
                                                                                                         'From Stundenzettel '
                                                                                                         'Where Freigabe is Null or Freigabe = 0 And BearbeiterID = '
                                                                                                         + str(session['Personalnummer']) + ' ))')

        elif wochentag == 6:
            return db.get_selected_information('SUM(Stunden) As SummeStd','Stundenzettel', 'DATEPART(dw,Datum) = 6 And ' +
                                                                                           'Datepart(wk,Datum) = '
                                                                                           'DATEPART(wk, (Select MAX(Datum) As Datum '
                                                                                                         'From Stundenzettel '
                                                                                                         'Where Freigabe is Null or Freigabe = 0 And BearbeiterID = '
                                                                                                         + str(session['Personalnummer']) + ' ))'
                                                                                           'And DATEPART(YYYY, Datum) = '
                                                                                           'DATEPART(YYYY, (Select MAX(Datum) As Datum '
                                                                                                         'From Stundenzettel '
                                                                                                         'Where Freigabe is Null or Freigabe = 0 And BearbeiterID = '
                                                                                                         + str(session['Personalnummer']) + ' ))')

        elif wochentag == 7:
            return db.get_selected_information('SUM(Stunden) As SummeStd','Stundenzettel', 'DATEPART(dw,Datum) = 7 And ' +
                                                                                           'Datepart(wk,Datum) = '
                                                                                           'DATEPART(wk, (Select MAX(Datum) As Datum '
                                                                                                         'From Stundenzettel '
                                                                                                         'Where Freigabe is Null or Freigabe = 0 And BearbeiterID = '
                                                                                                         + str(session['Personalnummer']) + ' ))'
                                                                                           'And DATEPART(YYYY, Datum) = '
                                                                                           'DATEPART(YYYY, (Select MAX(Datum) As Datum '
                                                                                                         'From Stundenzettel '
                                                                                                         'Where Freigabe is Null or Freigabe = 0 And BearbeiterID = '
                                                                                                         + str(session['Personalnummer']) + ' ))')

        else:
            print('Es gibt nur 7 Wochentage z.B. 1 = Montag ...')



    def validate_stundenzettel_date(self):

        db = DatabaseController()

        vonDatum = request.form.get('vonDatum', False)
        bisDatum = request.form.get('bisDatum', False)
        vonDatum = datetime.strptime(vonDatum, "%Y-%m-%d").strftime("%d.%m.%Y")
        bisDatum = datetime.strptime(bisDatum, "%Y-%m-%d").strftime("%d.%m.%Y")

        if vonDatum == None or bisDatum == None:

            vonDatum = ' '
            bisDatum = ' '

        info = ' and Convert(varchar, Datum, 104) >= ' + "'" + vonDatum + "'" + ' And Convert(varchar, Datum, 104) <= ' + "'" + bisDatum + "'"
        info = str(info)
        return info

    def get_kalenderwoche_stundenzettel(self):

        db = DatabaseController()
        info = ' '
        vonDatum = request.form.get('vonDatum', False)


        if vonDatum is not None:

            info = db.get_selected_information('datepart(wk, ' + "'" + vonDatum + "'" + ') AS Kalenderwoche')


        return info

    def get_vonDatum_Woche(self):

        db = DatabaseController()

        val = db.get_selected_information('DATEPART(dw,Getdate()) As vonDatum')

        if val[0]["vonDatum"] == 1:
            diff = str(7)
        elif val[0]["vonDatum"] == 2:
            diff = str(0)
        elif val[0]["vonDatum"] == 3:
            diff = str(-1)
        elif val[0]["vonDatum"] == 4:
            diff = str(-2)
        elif val[0]["vonDatum"] == 5:
            diff = str(-3)
        elif val[0]["vonDatum"] == 6:
            diff = str(-4)
        elif val[0]["vonDatum"] == 7:
            diff = str(-5)

        vonDatum = db.get_selected_information('Dateadd(dd, ' + diff + ' , GETDATE()) As vonDatum')
        vonDatum = str(vonDatum[0]["vonDatum"])
        vonDatum = datetime.strptime(vonDatum, "%Y-%m-%d %H:%M:%S.%f").strftime("%d.%m.%Y")

        return vonDatum

    def get_bisDatum_Woche(self):

        db = DatabaseController()

        val = db.get_selected_information('DATEPART(dw,Getdate()) As bisDatum')

        if val[0]["bisDatum"] == 1:
            diff = str(0)
        elif val[0]["bisDatum"] == 2:
            diff = str(6)
        elif val[0]["bisDatum"] == 3:
            diff = str(5)
        elif val[0]["bisDatum"] == 4:
            diff = str(4)
        elif val[0]["bisDatum"] == 5:
            diff = str(3)
        elif val[0]["bisDatum"] == 6:
            diff = str(2)
        elif val[0]["bisDatum"] == 7:
            diff = str(1)

        bisDatum = db.get_selected_information('Dateadd(dd, ' + diff + ' , GETDATE()) As bisDatum')
        bisDatum = str(bisDatum[0]["bisDatum"])
        bisDatum = datetime.strptime(bisDatum, "%Y-%m-%d %H:%M:%S.%f").strftime("%d.%m.%Y")

        return bisDatum