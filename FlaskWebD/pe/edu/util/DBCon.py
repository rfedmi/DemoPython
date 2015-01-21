# -*- coding: utf-8 -*-

'''
Created on 7/10/2014
#coding:utf-8
@author: Intel
'''

from flaskext.mysql import MySQL
from flask import Flask

class DBCon():
    
    def conexion(self):        
        mysql = MySQL()
        app = Flask(__name__)
        app.config['MYSQL_DATABASE_USER'] = 'python'
        app.config['MYSQL_DATABASE_PASSWORD'] = '123456'
        app.config['MYSQL_DATABASE_DB'] = 'ventas'
        app.config['MYSQL_DATABASE_HOST'] = 'localhost'
        mysql.init_app(app)
        
        return mysql
        
        
    def __init__(self):
        pass
        '''
        Constructor
        '''


'''cn=DBCon().conexion().connect()
with cn: 
    cursor = cn.cursor()
    cursor.execute("insert into personas (nombre, apell_paterno, apell_materno, dni, fecha_nacimiento, sexo, direccion, celular, estado) values('David', 'Mamani', 'Pari', '43631214', '2014-02-02','M', 'ver', '951782520', 1)")

print "si llego"     '''
        
        