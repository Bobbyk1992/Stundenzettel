from flask import session
from os import getenv
import pymssql
import time

"""server = getenv("127.0.0.1\SQLEXPRESS")
user = getenv("sa")
password = getenv("Achilles")"""

server = r'Desktop-3BRBS77\Sqlexpress'
user = r'sa'
password = 'Achilles'

conn = pymssql.connect(host=server, user=user, password=password, database="Zeiterfassung")
cursor = conn.cursor()
"""cursor.execute('Select * From LoginProtokoll')"""
cursor.execute("Insert Into LoginProtokoll(Gescannt, Personalnummer , Zeitpunkt) Values ('GH34', 12, CURRENT_TIMESTAMP)")
conn.commit()

"""for row in cursor:
    print('row = %r' % (row,))"""

"""print(cursor.fetchall())"""

conn.close()
