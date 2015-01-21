# -*- coding: utf-8 -*-

from flask import Flask,redirect,url_for, request
from flask.templating import render_template
from pe.edu.util import DBCon
import sys

app=Flask(__name__)
cn=DBCon.DBCon()

@app.route("/")
def inicio():
    print "Welcome to Python Flask App! DMP Ñaño"
    cursor=cn.conexion().connect().cursor()   
    cursor.execute("SELECT idpersona, nombre, apell_paterno, apell_materno, dni, fecha_nacimiento, sexo, direccion, celular, estado FROM personas ")
    rows = cursor.fetchall()
    contador=0
    for row in rows:
        print row          
    return render_template("index.html", newsitems=rows,cont=contador)

@app.route("/add")
def verPersona():
    cursor=cn.conexion().connect().cursor()   
    cursor.execute("SELECT * from personas")
    rows = cursor.fetchall()
    for row in rows:
        print row        
    return redirect(url_for('inicio'))

@app.route("/eliminar")
def eliminarPersona():   
    idpersona = int(request.args.get('idpersona'))
    sql="""delete from personas where idpersona= %i """ % (idpersona)    
    con=cn.conexion().connect()
    with con:         
        try:
            cursor = con.cursor()
            cursor.execute(sql)
        except:
            print("Error inesperado al eliminar:", sys.exc_info()[0])
                 
    return redirect(url_for('inicio'))

@app.route("/editar")
def editarPersona():
    idpersona = int(request.args.get('idpersona'))
    sql="""SELECT * from personas  where idpersona= %i """ % (idpersona)
    cursor=cn.conexion().connect().cursor()   
    cursor.execute(sql)
    rows = cursor.fetchall()
    
    for row in rows:
        print row        
    return render_template("editForm.html", newsitems=rows)

@app.route("/buscar")
def buscarDataPersona():
    nombre = (request.args.get('nombrebuscar'))
    sql="""SELECT * FROM personas  WHERE UPPER(CONCAT(nombre,' ',apell_paterno,' ', apell_materno)) LIKE UPPER('%s')  """ % ("%"+nombre+"%")
    cursor=cn.conexion().connect().cursor()   
    cursor.execute(sql)
    rows = cursor.fetchall()
    
    for row in rows:
        print row        
    return render_template("index.html", newsitems=rows)

@app.route("/agregar")
def addPersona():
    nombre = request.args.get('nombre')
    print nombre  
    print "ñoño"   
    apellpat = (request.args.get('apellpat'))
    apellmat = (request.args.get('apellmat'))
    dni = str(request.args.get('dni'))
    fnacimiento = str(request.args.get('fnacimiento'))
    sexo = str(request.args.get('sexo'))
    celular = str(request.args.get('celular'))
    estado = int(request.args.get('estado'))
    directhion = (request.args.get('directhion'))     
    print fnacimiento
    sql="""insert into personas(nombre, apell_paterno, apell_materno, dni, fecha_nacimiento, sexo, direccion, celular, estado) values('%s','%s','%s','%s','%s','%s','%s','%s',%i)""" % (nombre, apellpat,apellmat, dni, fnacimiento,sexo,directhion,celular,estado)
    print sql
    con=cn.conexion().connect()
    with con:         
        try:
            cursor = con.cursor()
            cursor.execute(sql)
        except:
            print("Error inesperado:", sys.exc_info()[0])
                  
    return redirect(url_for('inicio'))

@app.route("/actualizar")
def updatePersona():
    nombre = (request.args.get('nombre'))
    idpersona=int(request.args.get('idpersona'))
    apellpat = (request.args.get('apellpat'))
    apellmat = (request.args.get('apellmat'))
    dni = str(request.args.get('dni'))
    fnacimiento = str(request.args.get('fnacimiento'))
    sexo = str(request.args.get('sexo'))
    celular = str(request.args.get('celular'))
    estado = int(request.args.get('estado'))
    directhion = str(request.args.get('directhion'))     
    print fnacimiento
    sql="""UPDATE personas SET nombre = '%s' , apell_paterno = '%s' , apell_materno = '%s' , dni = '%s' , fecha_nacimiento = '%s' , sexo = '%s' , direccion = '%s' , celular = '%s' , estado = %i WHERE idpersona = %i """  % (nombre, apellpat,apellmat, dni, fnacimiento,sexo,directhion,celular,estado,idpersona)
    print sql
    con=cn.conexion().connect()
    with con:         
        try:
            cursor = con.cursor()
            cursor.execute(sql)
        except:
            print("Error inesperado al acualizar:", sys.exc_info()[0])
        
    return redirect(url_for('inicio'))

if __name__=="__main__":
    app.run()