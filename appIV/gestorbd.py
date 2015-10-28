#!/usr/bin/python3
# -*- coding: utf-8 -*-

import MySQLdb


class Empresa:

    def __init__(self):
        self.ID = ""
        self.nombre = ""

class Usuario:

    def __init__(self):
        self.nombre = ""

class Calificacion:

    def __init__(self):
        self.nombre = ""
        self.ID = ""
        self.nota= ""




class GestorEmpresa:

    @classmethod
    def nuevaEmpresa(self, ID, nombre):
        db = MySQLdb.connect(host="localhost", user="root", db="mdb")

        sel= "Select count(*) from Empresa where (ID ='"+str(ID)+"');"
        query="INSERT INTO Empresa values("+"'"+str(ID)+"', "+"'"+nombre+"');"
        
        cursor = db.cursor()
        
        cursor.execute(sel)
        existe=int(cursor.fetchone()[0])
        
        if existe==0:
        	cursor.execute(query)
        
        db.commit()
        cursor.close()
        db.close()

    @classmethod
    def getEmpresas(self):
        db = MySQLdb.connect(host="localhost", user="root", db="mdb");

        cursor = db.cursor()
        query="select * from Empresa";
        cursor.execute(query);
        row = cursor.fetchone()

        lista = []

        while row is not None:
            empresa = Empresa()
            empresa.ID=row[0]
            empresa.nombre=row[1]
            lista.append(empresa)
            #print row[0], row[1]
            row = cursor.fetchone()

        cursor.close()
        db.close()

        return lista

'''
    @classmethod
    def borrarEmpresa(self, ident):
        db = MySQLdb.connect(host="localhost", user="root", passwd="root", db="mdb"); #La conexión está clara.
        query="DELETE FROM Empresa WHERE ID="+ident+";"
        cursor = db.cursor()
        cursor.execute(query);
        db.commit()
        cursor.close()
        db.close()
''' 

class GestorUsuario:

    @classmethod
    def nuevoUsuario(self, nombre):
        db = MySQLdb.connect(host="localhost", user="root", db="mdb")

        sel= "Select count(*) from Usuario where (nombre_u ='"+nombre+"');"
        query="INSERT INTO Usuario values("+"'"+nombre+"');"
        
        cursor = db.cursor()
        
        cursor.execute(sel)
        existe=int(cursor.fetchone()[0])
        
        if existe==0:
        	cursor.execute(query)
        
        db.commit()
        cursor.close()
        db.close()

    @classmethod
    def getUsuarios(self):
        db = MySQLdb.connect(host="localhost", user="root", db="mdb");

        cursor = db.cursor()
        query="select * from Usuario";
        cursor.execute(query);
        row = cursor.fetchone()

        lista = []

        while row is not None:
            user = Usuario()
            user.nombre=row[0]
            lista.append(user)
            #print row[0], row[1]
            row = cursor.fetchone()

        cursor.close()
        db.close()

        return lista

class GestorCalificar:

    @classmethod
    def nuevaCali(self, nombre_u, ID, nota):
        db = MySQLdb.connect(host="localhost", user="root", db="mdb")
        gs=GestorUsuario()
        sel_c= "SELECT count(*) from Califica where nombre_u ="+"'"+nombre_u+"' AND ID='"+str(ID)+"';"
        sel_e= "SELECT count(*) from Empresa where (ID ="+"'"+str(ID)+"');"
        query="INSERT INTO Califica values("+"'"+nombre_u+"', '"+str(ID)+"', '"+str(nota)+"');"
        
        cursor = db.cursor()
        
        cursor.execute(sel_c)
        existe_c=int(cursor.fetchone()[0])
        cursor.execute(sel_e)
        existe_e=int(cursor.fetchone()[0])
        
        if existe_c==0 and existe_e>0:
        	gs.nuevoUsuario(nombre_u)
        	cursor.execute(query)
        
        db.commit()
        cursor.close()
        db.close()	

    @classmethod
    def borrarCali(self, nombre_u, ID):
        db = MySQLdb.connect(host="localhost", user="root", db="mdb")

        sel_c= "SELECT count(*) from Califica where nombre_u ="+"'"+nombre_u+"' AND ID='"+str(ID)+"';"
        query="DELETE FROM Califica where nombre_u ="+"'"+nombre_u+"' AND ID='"+str(ID)+"';"
        
        cursor = db.cursor()


        cursor.execute(sel_c)
        existe_c=int(cursor.fetchone()[0])
        

        if existe_c>0 :
        	cursor.execute(query)
        
        db.commit()
        cursor.close()
        db.close()


    @classmethod
    def getCalis(self):
        db = MySQLdb.connect(host="localhost", user="root", db="mdb");

        cursor = db.cursor()
        query="select * from Califica";
        cursor.execute(query);
        row = cursor.fetchone()

        lista = []

        while row is not None:
            cal = Calificacion()
            cal.ID=row[1]
            cal.nombre=row[0]
            cal.nota=row[2]
            lista.append(cal)
            #print row[0], row[1]
            row = cursor.fetchone()

        cursor.close()
        db.close()

        return lista