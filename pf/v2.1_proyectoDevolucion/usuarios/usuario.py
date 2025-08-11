from conexionBD import *
import datetime
import hashlib

def hash_password(contrasena):
    return hashlib.sha256(contrasena.encode()).hexdigest()



def registrar(nombre,apellido,email,contrasena,id_roles):
    try:
        fecha = datetime.datetime.now()
        contrasena=hash_password(contrasena)
        sql = "INSERT INTO usuarios (nombre, apellidos, email, password, fecha, id_roles) VALUES (%s, %s, %s, %s, %s, %s)"
        val = (nombre, apellido, email, contrasena, fecha, id_roles)
        cursor.execute(sql, val)
        conexion.commit()
        return True
    except:
        return False


def iniciarSesion(correo, contrasena):
    try:
        contrasena = hash_password(contrasena)
        sql = "SELECT id, nombre, apellidos, id_roles FROM usuarios WHERE email=%s AND password=%s"
        val = (correo, contrasena)
        cursor.execute(sql, val)
        return cursor.fetchone()  # Retornará (id, nombre, apellidos) o None
    except:
        return None