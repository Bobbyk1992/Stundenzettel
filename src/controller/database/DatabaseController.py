from flask import session
from os import getenv
import pymssql
import time
from src.controller.Controller import Controller


class DatabaseController(Controller):

    def __init__(self, server='localhost\Sqlexpress', user=r'sa', password='Achilles', db='Stundenzettel'):

        self.dbserver = server
        self.dbuser = user
        self.dbpassword = password
        self.dbname = db
        self.client = pymssql.connect(host=self.dbserver, user=self.dbuser, password=self.dbpassword,
                                      database=self.dbname, as_dict=True, autocommit=True)
        self.cursor = self.client.cursor()

    def get_many_information(self, table, where):

            self.cursor.execute('Select * FROM ' + table + ' where ' + where)
            tables = self.cursor.fetchall()
            return tables

    def get_one_information(self, table):

            self.cursor.execute(' Select * FROM ' + table)
            tables = self.cursor.fetchall()
            return tables

    def get_selected_information(self, field, table=None, where=None):

          if where is not None and table is not None and field is not None:
                self.cursor.execute('Select ' + field + ' FROM ' + table + ' where ' + where)
                tables = self.cursor.fetchall()
                return tables

          elif where is None and table is not None and field is not None:
                self.cursor.execute('Select ' + field + ' FROM ' + table)
                tables = self.cursor.fetchall()
                return tables

          elif where is None and table is None and field is not None:
                self.cursor.execute('Select ' + field )
                tables = self.cursor.fetchall()
                return tables

          else:
              print('Du hast keine Parameter übergeben!!!')

    def insert_information(self, table, col, val):

        self.cursor.execute('Insert Into ' + table + ' (' + col + ' ) Values (' + val + ' )')

    def update_information(self, table, set, where=None):

        if where is not None:
            self.cursor.execute('Update ' + table + ' Set ' + set + ' where ' + where)
        else:
            self.cursor.execute('Update ' + table + ' Set ' + set)

    def column_string(self, col):

        if col is not None:
            wrap_col_str = "'" + col + "'"
        else:
            wrap_col_str = None

        return wrap_col_str

"""client = pymssql.connect(host='Desktop-3BRBS77\Sqlexpress', user=r'sa', password='Achilles',
                                      database='Stundenzettel')

cursor = client.cursor()

cursor.execute(' Select * FROM Mitarbeiter ')
row = cursor.fetchone()
while row:
    print(row)
    row = cursor.fetchone()"""