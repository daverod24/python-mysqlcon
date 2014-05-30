#!/usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb as mdb
import sys


var = raw_input("Ingrese el usuario root de su BD Mysql: ")
var1 = raw_input("Ingrese el password del usuario root de su BD Mysql : ")


con = mdb.connect('localhost', var, var1);

with con:

    cur = con.cursor()
    cur.execute("DROP DATABASE if exists pruebadb")  ## Elimina la BD si existe
    cur.execute("CREATE DATABASE pruebadb")  ## Crea la BD
    cur.execute("DROP USER 'usuarioprueba'@'localhost'") ## Borra el usuario para evitar error si ya esta creado
    cur.execute("CREATE USER 'usuarioprueba'@'localhost' IDENTIFIED BY '123'") ## crea el usuario de la base de datos
    cur.execute("GRANT ALL ON *.* TO 'usuarioprueba'@'localhost'") ## le da permisos


