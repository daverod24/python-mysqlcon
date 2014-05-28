#!/usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb as mdb

con = mdb.connect('localhost', 'usuarioprueba', '123', 'pruebadb');

with con:

    cur = con.cursor()
    cur.execute("SELECT * FROM Trabajadores")

    rows = cur.fetchall()

    for row in rows:
        print row
