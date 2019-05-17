from flask import session
from os import getenv
import pymssql
import time
from ..Controller import Controller

class DatabaseController(Controller):

    def __init__(self, server=r'Desktop-3BRBS77\Sqlexpress' , user=r'sa', password='Achilles', db='Zeiterfassung'):

        self.dbserver = server
        self.dbuser = user
        self.dbpassword = password
        self.dbname = db
        self.client = pymssql.connect(host=self.dbserver, user=self.dbuser, password=self.dbpassword, database=self.dbname)
        self.cursor = self.client.cursor()

    def get_information(self, table, where):

        if where:
            self.cursor.execute('Select * FROM ' & table &  'where ' & where )

        else:
            self.cursor.execute('Select * FROM ' & table)

    def insert_information(self, table, col, val):

        self.cursor.execute('Insert Into ' & table & ' (' & col & ' ) Values (' & val & ' )')


