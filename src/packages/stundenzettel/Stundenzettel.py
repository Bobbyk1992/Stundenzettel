from src.packages.stundenzettel.abstract.AbstractStundenzettel import AbstractStundenzettel
from src.controller.database.DatabaseController import DatabaseController
from flask import session, request, url_for
from datetime import datetime

class Stundenzettel(AbstractStundenzettel):

    def __init__(self):
        super().__init__()

    def wochentag_summe(self, wochentag):

        db = DatabaseController()
        vonDatum = self.get_vonDatum_Woche()
        bisDatum = self.get_bisDatum_Woche()

        if wochentag == 1:
            return db.get_selected_information('SUM(Stunden) As SummeStd','Stundenzettel', 'DATEPART(dw,Datum) = 1 And ' +
                                                                                            '(Freigabe is Null or Freigabe = 0) And BearbeiterID = '
                                                                                            + str(session['Personalnummer']) +
                                                                                            ' and Convert(varchar, Datum, 104) >= ' + "'" + vonDatum + "'" +
                                                                                            ' And Convert(varchar, Datum, 104) <= ' + "'" + bisDatum + "'")

        elif wochentag == 2:
            return db.get_selected_information('SUM(Stunden) As SummeStd','Stundenzettel', 'DATEPART(dw,Datum) = 2 And ' +
                                                                                            '(Freigabe is Null or Freigabe = 0) And BearbeiterID = '
                                                                                            + str(session['Personalnummer']) +
                                                                                            ' and Convert(varchar, Datum, 104) >= ' + "'" + vonDatum + "'" +
                                                                                            ' And Convert(varchar, Datum, 104) <= ' + "'" + bisDatum + "'")
        elif wochentag == 3:
            return db.get_selected_information('SUM(Stunden) As SummeStd','Stundenzettel', 'DATEPART(dw,Datum) = 3 And ' +
                                                                                            '(Freigabe is Null or Freigabe = 0) And BearbeiterID = '
                                                                                            + str(session['Personalnummer']) +
                                                                                            ' and Convert(varchar, Datum, 104) >= ' + "'" + vonDatum + "'" +
                                                                                            ' And Convert(varchar, Datum, 104) <= ' + "'" + bisDatum + "'")
        elif wochentag == 4:
            return db.get_selected_information('SUM(Stunden) As SummeStd','Stundenzettel', 'DATEPART(dw,Datum) = 4 And ' +
                                                                                            '(Freigabe is Null or Freigabe = 0) And BearbeiterID = '
                                                                                            + str(session['Personalnummer']) +
                                                                                            ' and Convert(varchar, Datum, 104) >= ' + "'" + vonDatum + "'" +
                                                                                            ' And Convert(varchar, Datum, 104) <= ' + "'" + bisDatum + "'")

        elif wochentag == 5:
            return db.get_selected_information('SUM(Stunden) As SummeStd','Stundenzettel', 'DATEPART(dw,Datum) = 5 And ' +
                                                                                            '(Freigabe is Null or Freigabe = 0) And BearbeiterID = '
                                                                                            + str(session['Personalnummer']) +
                                                                                            ' and Convert(varchar, Datum, 104) >= ' + "'" + vonDatum + "'" +
                                                                                            ' And Convert(varchar, Datum, 104) <= ' + "'" + bisDatum + "'")

        elif wochentag == 6:
            return db.get_selected_information('SUM(Stunden) As SummeStd','Stundenzettel', 'DATEPART(dw,Datum) = 6 And ' +
                                                                                            '(Freigabe is Null or Freigabe = 0) And BearbeiterID = '
                                                                                            + str(session['Personalnummer']) +
                                                                                            ' and Convert(varchar, Datum, 104) >= ' + "'" + vonDatum + "'" +
                                                                                            ' And Convert(varchar, Datum, 104) <= ' + "'" + bisDatum + "'")

        elif wochentag == 7:
            return db.get_selected_information('SUM(Stunden) As SummeStd','Stundenzettel', 'DATEPART(dw,Datum) = 7 And ' +
                                                                                            '(Freigabe is Null or Freigabe = 0) And BearbeiterID = '
                                                                                            + str(session['Personalnummer']) +
                                                                                            ' and Convert(varchar, Datum, 104) >= ' + "'" + vonDatum + "'" +
                                                                                            ' And Convert(varchar, Datum, 104) <= ' + "'" + bisDatum + "'")

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

    def get_kalenderwoche_stundenzettel(self, datum):

        db = DatabaseController()
        info = ' '
        #vonDatum = request.form.get(datum, False)


        #if vonDatum is not None:

        info = db.get_selected_information('datepart(wk, Convert(datetime, ' + "'" + datum + "'" + ' ,104)) AS Kalenderwoche')


        return info

    def get_vonDatum_Woche(self):

        db = DatabaseController()

        data = db.get_selected_information('*', 'Stundenzettel', '(Freigabe is Null or Freigabe = 0) And BearbeiterID = ' + str(session['Personalnummer']))


        #datum = db.get_selected_information('Convert(varchar, MAX(Datum) , 104) As Datum', 'Stundenzettel', 'Freigabe is Null or Freigabe = 0 And BearbeiterID = '
         #                                                                  + str(session['Personalnummer']) )
        #datum = str(datum[0]["Datum"])
        #datum = datetime.strptime(datum, "%Y-%m-%d %H:%M:%S").strftime("%Y-%m-%d %H:%M:%S.%f")

        if len(data) == 0:
            val = db.get_selected_information('DATEPART(dw, MAX(Datum) ) As vonDatum', 'Stundenzettel',
                                              'Freigabe = -1 And BearbeiterID = '
                                              + str(session['Personalnummer']))

        else:
            val = db.get_selected_information('DATEPART(dw, MAX(Datum) ) As vonDatum', 'Stundenzettel', '(Freigabe is Null or Freigabe = 0) And BearbeiterID = '
                                                                           + str(session['Personalnummer']) )

        if val[0]["vonDatum"] == 1:
            diff = str(-6)
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

        if len(data) == 0:
            diff = int(diff) +7
            diff = str(diff)
            vonDatum = db.get_selected_information('Dateadd(dd, ' + diff + ' , MAX(Datum)) As vonDatum',
                                                   'Stundenzettel',
                                                   'Freigabe = -1 And BearbeiterID = '
                                                   + str(session['Personalnummer']))

        else:
            vonDatum = db.get_selected_information('Dateadd(dd, ' + diff + ' , MAX(Datum)) As vonDatum', 'Stundenzettel', '(Freigabe is Null or Freigabe = 0) And BearbeiterID = '
                                                                           + str(session['Personalnummer']) )

        vonDatum = str(vonDatum[0]["vonDatum"])
        vonDatum = datetime.strptime(vonDatum, "%Y-%m-%d %H:%M:%S").strftime("%d.%m.%Y")

        return vonDatum

    def get_bisDatum_Woche(self):

        db = DatabaseController()

        data = db.get_selected_information('*', 'Stundenzettel' , '(Freigabe is Null or Freigabe = 0) And BearbeiterID = ' + str(session['Personalnummer']))

        #datum = db.get_selected_information('MAX(Datum) as Datum ', 'Stundenzettel', 'Freigabe is Null or Freigabe = 0 And BearbeiterID = '
        #                                                                   + str(session['Personalnummer']))
        #datum = str(datum[0]["Datum"])
        #datum = datetime.strptime(datum, "%Y-%m-%d %H:%M:%S").strftime("%Y-%m-%d %H:%M:%S.%f")

        if len(data) == 0:
            val = db.get_selected_information('DATEPART(dw, MAX(Datum) ) As bisDatum', 'Stundenzettel',
                                              'Freigabe = -1 And BearbeiterID = '
                                              + str(session['Personalnummer']))

        else:
            val = db.get_selected_information('DATEPART(dw, MAX(Datum) ) As bisDatum', 'Stundenzettel', '(Freigabe is Null or Freigabe = 0) And BearbeiterID = '
                                                                                                    + str(session['Personalnummer']))
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

        if len(data) == 0:
            diff = int(diff) +7
            diff = str(diff)
            bisDatum = db.get_selected_information('Dateadd(dd, ' + diff + ' , MAX(Datum)) As bisDatum',
                                                   'Stundenzettel',
                                                   'Freigabe = -1 And BearbeiterID = '
                                                   + str(session['Personalnummer']))

        else:
            bisDatum = db.get_selected_information('Dateadd(dd, ' + diff + ' , MAX(Datum)) As bisDatum',
                                                   'Stundenzettel', '(Freigabe is Null or Freigabe = 0) And BearbeiterID = '
                                                   + str(session['Personalnummer']) )

        bisDatum = str(bisDatum[0]["bisDatum"])
        bisDatum = datetime.strptime(bisDatum, "%Y-%m-%d %H:%M:%S").strftime("%d.%m.%Y")

        return bisDatum

    def save_leistung(self):

        db = DatabaseController()

        personalnummer = str(session['Personalnummer'])

        datum = request.form.get('LeistDatum', False)
        datum = datetime.strptime(datum, "%Y-%m-%d").strftime("%d.%m.%Y")
        #datum = datum + ' 00:00:00.000'
        objektnr = request.form.get('LeistObjektnummer', None)

        objektname = request.form.get('LeistObjektname', None)
        objektname = db.column_string(objektname)

        objektstrasse = request.form.get('LeistObjektstrasse', None)
        objektstrasse = db.column_string(objektstrasse)

        objektplz = request.form.get('LeistPLZ', None)
        objektplz = db.column_string(objektplz)

        objektort = request.form.get('LeistOrt', None)
        objektort = db.column_string(objektort)

        titel = request.form.get('LeistTitel_Nr', None)
        untertitel = request.form.get('LeistUntertitel_Nr', None)

        leistung = request.form.get('LeistLeistung', None)
        leistung = db.column_string(leistung)

        stunden = request.form.get('LeistStunden', None)

        bemerkung = request.form.get('LeistBemerkung', None)
        bemerkung = db.column_string(bemerkung)

        result = db.insert_information('Stundenzettel',
                                  'BearbeiterID, Datum, Objektnr, Objektname, Objektstrasse, ObjektPLZ, ObjektOrt, Titel_Nr, Untertitel_Nr, Leistung, Stunden, Bemerkung',
                                    personalnummer + ', '
                                    + "Convert(datetime, '" + datum + "', 104 )" + ', '
                                    + objektnr + ', '
                                    +  objektname + ', '
                                    +  objektstrasse  + ', '
                                    + objektplz  + ', '
                                    + objektort  + ', '
                                    + titel + ', '
                                    + untertitel + ', '
                                    + leistung + ', '
                                    + stunden + ', '
                                    +  bemerkung )

        return result

    def save_reisekosten(self):

        db = DatabaseController()

        personalnummer = str(session['Personalnummer'])

        datum = request.form.get('ReisekostenDatum', False)
        datum = datetime.strptime(datum, "%Y-%m-%d").strftime("%d.%m.%Y")
        # datum = datum + ' 00:00:00.000'
        objektnr = request.form.get('ReisekostenObjektnummer', None)

        objektname = request.form.get('ReisekostenObjektname', None)
        objektname = db.column_string(objektname)

        objektstrasse = request.form.get('ReisekostenObjektstrasse', None)
        objektstrasse = db.column_string(objektstrasse)

        objektplz = request.form.get('ReisekostenPLZ', None)
        objektplz = db.column_string(objektplz)

        objektort = request.form.get('ReisekostenOrt', None)
        objektort = db.column_string(objektort)

        reiseart = request.form.get('ReisekostenTitel', None)

        titel = request.form.get('ReisekostenTitel', None)
        untertitel = request.form.get('ReisekostenUntertitel', None)

        ziel = request.form.get('ReisekostenZiel', None)
        ziel = db.column_string(ziel)

        privat = request.form.get('ReisekostenPrivat', None)
        privat = db.column_string(privat)

        zweck = request.form.get('ReisekostenZweck', None)
        zweck = db.column_string(zweck)

        bemerkung = request.form.get('ReisekostenBemerkung', None)
        bemerkung = db.column_string(bemerkung)

        stunden = '0'
        stunden = db.column_string(stunden)

        leistung = '-'
        leistung = db.column_string(leistung)

        result = db.insert_information('Stundenzettel',
                                       'BearbeiterID, Datum, Objektnr, Objektname, Objektstrasse, ObjektPLZ, ObjektOrt, Reise_Art ,Titel_Nr, Untertitel_Nr, Ziel, PG, Zweck, Bemerkung, Stunden, Leistung',
                                       personalnummer + ', '
                                       + "Convert(datetime, '" + datum + "', 104 )" + ', '
                                       + objektnr + ', '
                                       + objektname + ', '
                                       + objektstrasse + ', '
                                       + objektplz + ', '
                                       + objektort + ', '
                                       + reiseart + ', '
                                       + titel + ', '
                                       + untertitel + ', '
                                       + ziel + ', '
                                       + privat + ', '
                                       + zweck + ', '
                                       + bemerkung + ', '
                                       + stunden + ', '
                                       + leistung)

        return result


    def save_sonstiges(self):

        db = DatabaseController()

        personalnummer = str(session['Personalnummer'])

        datum = request.form.get('SonstigesDatum', False)
        datum = datetime.strptime(datum, "%Y-%m-%d").strftime("%d.%m.%Y")

        leistung = request.form.get('SonstigeLeistung', None)
        leistung = db.column_string(leistung)

        urlaub =  request.form.get('SonstigeUrlaub', 0)
        krankheit = request.form.get('SonstigeKrankheit', 0)
        freizeit = request.form.get('SonstigeFreizeit', 0)

        if leistung == 'Urlaub':
            urlaub = -1
            krankheit = 0
            freizeit = 0

        if leistung == 'Krank' or leistung == 'Arztbesuche':
            krankheit = -1
            urlaub = 0
            freizeit = 0

        if leistung == 'Freizeitausgleich v. Überstunden':
            freizeit = -1
            krankheit = 0
            urlaub = 0

        urlaub = str(urlaub)
        krankheit = str(krankheit)
        freizeit = str(freizeit)

        bemerkung = request.form.get('SonstigeBemerkung', None)
        bemerkung = db.column_string(bemerkung)

        stunden = request.form.get('SonstigeStunden', None)

        beschreibung = request.form.get('SonstigeBeschreibung', None)
        beschreibung = db.column_string(beschreibung)

        untertitel = '-'
        untertitel = db.column_string(untertitel)

        titel = '-'
        titel = db.column_string(titel)

        objektnr = '0'
        objektnr = db.column_string(objektnr)
        objektname = '-'
        objektname = db.column_string(objektname)

        result = db.insert_information('Stundenzettel',
                                       'BearbeiterID, Datum, Leistung, Urlaub, Krankheit, Freizeitausgleich, Bemerkung, Stunden, Zusatzinfo, Untertitel_Nr, Titel_Nr, Objektnr, Objektname',
                                       personalnummer + ', '
                                       + "Convert(datetime, '" + datum + "', 104 )" + ', '
                                       + leistung + ', '
                                       + urlaub + ', '
                                       + krankheit + ', '
                                       + freizeit + ', '
                                       + bemerkung + ', '
                                       + stunden + ', '
                                       + beschreibung + ', '
                                       + untertitel + ', '
                                       + titel + ', '
                                       + objektnr + ', '
                                       + objektname)

        return result



    def get_edit_day(self):

        db = DatabaseController()

        data = db.get_selected_information('*', 'Stundenzettel',
                                           '(Freigabe is Null or Freigabe = 0) And BearbeiterID = ' + str(
                                               session['Personalnummer']))

        if len(data) == 0:
            edit_day = self.get_vonDatum_Woche()
            edit_day = datetime.strptime(edit_day, "%d.%m.%Y").strftime("%Y-%m-%d")


        else:
            edit_day = db.get_selected_information('Max(Datum) As Datum', 'Stundenzettel', 'Freigabe is Null or Freigabe = 0 And BearbeiterID = '
                                                                                       + str(session['Personalnummer']))

            edit_day = str(edit_day[0]["Datum"])
            edit_day = datetime.strptime(edit_day, "%Y-%m-%d %H:%M:%S").strftime("%Y-%m-%d")

        return edit_day

    def freigabe_stundenzettel(self):

        db = DatabaseController()

        vonDatum = self.get_vonDatum_Woche()
        bisDatum = self.get_bisDatum_Woche()

        freigabe = db.update_information('Stundenzettel', 'Freigabe= -1', '(Freigabe is Null or Freigabe = 0) And BearbeiterID = ' + str(session['Personalnummer']) + ' and Convert(varchar, Datum, 104) >= ' + "'" + vonDatum + "'" + ' And Convert(varchar, Datum, 104) <= ' + "'" + bisDatum + "'" )

