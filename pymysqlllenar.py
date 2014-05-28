#!/usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb as mdb

con = mdb.connect('localhost', 'usuarioprueba', '123', 'pruebadb');

with con:

    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS Trabajadores")
    cur.execute("CREATE TABLE Trabajadores(Id INT PRIMARY KEY AUTO_INCREMENT, \
                 Name VARCHAR(25))")
    cur.execute("INSERT INTO Trabajadores(Name) VALUES('Juan Ramirez')")
    cur.execute("INSERT INTO Trabajadores(Name) VALUES('Pedro perez')")
    cur.execute("INSERT INTO Trabajadores(Name) VALUES('Maria garcia')")
    cur.execute("INSERT INTO Trabajadores(Name) VALUES('Javier galindo')")
    cur.execute("INSERT INTO Trabajadores(Name) VALUES('Rafael Ortiz')")
