from conexionBD import *
import datetime

def registrar_usuario(nombre, apellidos, email, password):
    try:
        fecha=datetime.datetime.now()
        sql="insert into usuarios (nombre, apellidos, email, password, fecha) values (%s, %s, %s, %s, %s)"
        val=(nombre, apellidos, email, password)
        cursor.execute(sql, val)
        return True
    except:
        return False

def inicio_sesion(email, password):
    try:
        sql="select * from usuarios where email = %s and password = %s"
        val=(email, password)
        cursor.execute(sql, val)
        registro=cursor.fetchone()
        if registro:
            return registro
        else:
            return None
    except:
        return None