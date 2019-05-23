from flask import session
from os import getenv
import pymssql
import time
from src.controller.Controller import Controller


class DatabaseController(Controller):

    def __init__(self, server='Desktop-3BRBS77\Sqlexpress', user=r'sa', password='Achilles', db='Stundenzettel'):

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

    def get_selected_information(self, field, table, where):

            self.cursor.execute('Select ' + field + ' FROM ' + table + ' where ' + where)
            tables = self.cursor.fetchall()
            return tables

    def insert_information(self, table, col, val):

        self.cursor.execute('Insert Into ' & table & ' (' & col & ' ) Values (' & val & ' )')

"""client = pymssql.connect(host='Desktop-3BRBS77\Sqlexpress', user=r'sa', password='Achilles',
                                      database='Stundenzettel')

cursor = client.cursor()

cursor.execute(' Select * FROM Mitarbeiter ')
row = cursor.fetchone()
while row:
    print(row)
    row = cursor.fetchone()"""