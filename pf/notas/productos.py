from conexionBD import *
from funciones import esperarTecla
def devolver(nombre1, problema, precio, id_categoria, id_usuario):
    try:
        cursor.execute(
            "INSERT INTO productos (nombre, problema, precio, fecha, id_categoria, id_usuario) VALUES (%s, %s, %s, NOW(), %s, %s)",
            (nombre1, problema, precio, id_categoria, id_usuario)
        )
        conexion.commit()
        return True
    except Exception as e:
        print("Error en devolución:", e)
        return False

def categorias():
    try:
        cursor.execute("SELECT * FROM categorias")
        categorias = cursor.fetchall()
        
        if len:
                print("categorias")
                print(f"{'ID':<10}{'Categorias':<15}")######aqui me quede tegno que hacer que se muetre las categorias arriba par apoder selccionar una ala de devolver un prdcto
                print(f"-"*100)
                for fila in categorias:
                    print(f"{fila[0]:<10}{fila[1]:<15}")
                print(f"-"*100)  
    except:
        return False
    
def mostrar(id_usuario):
    try:
        consulta = """
            SELECT 
                p.id, 
                p.nombre, 
                p.problema, 
                p.precio, 
                c.categorias,  -- nombre de la categoría aquiii va eso para no se te olvide addy
                p.fecha
            FROM productos p
            JOIN categorias c ON p.id_categoria = c.id
            WHERE p.id_usuario = %s
        """
        cursor.execute(consulta, (id_usuario,))
        productos = cursor.fetchall()
        return productos
    except:
        return False
    


def mostrarAdmin():
    try:
        cursor = conexion.cursor(dictionary=True)

        consulta = """
            SELECT 
                p.id,
                p.nombre AS nombre_producto,
                p.problema,
                p.precio,
                u.nombre AS nombre_usuario,
                c.categorias AS nombre_categoria,
                p.fecha
            FROM productos p
            JOIN usuarios u ON p.id_usuario = u.id
            JOIN categorias c ON p.id_categoria = c.id
        """
        cursor.execute(consulta)
        resultado = cursor.fetchall()
        return resultado
    except:
        return []



def buscarProducto(id_usuario,productos,id_categoria):
    try:
        


        return True
    except:
        return False


def mostrarUsuarios():
    try:
        cursor.execute("SELECT id, nombre, apellidos FROM usuarios")
        lista_usuarios = cursor.fetchall()
        

        return lista_usuarios
    except :
        return False

def mostrarProductosPorUsuario(id_usuario):
    try:
        consulta = """
            SELECT 
                p.id, 
                p.nombre, 
                p.problema, 
                p.precio, 
                c.categorias,  -- nombre de la categoría aquiii va eso para no se te olvide addy
                p.fecha
            FROM productos p
            JOIN categorias c ON p.id_categoria = c.id
            WHERE p.id_usuario = %s
        """
        cursor.execute(consulta, (id_usuario,))
        productos = cursor.fetchall()
        return productos
    except:
        return False

def borrar(id):
    try:
        cursor.execute("delete from productos where id=%s",(id,))
        conexion.commit()
        return True
    except:
        return False

def motivoEliminacion(razon, id, id_usuario):
    try:
        cursor.execute("SELECT nombre FROM productos WHERE id = %s", (id,))
        resultado = cursor.fetchone()
        if resultado:
            nombre_producto = resultado[0]
            mensaje = f"{razon}"
        else:
            nombre_producto = "Desconocido"
            mensaje = f"{razon}"
        cursor.execute(
            "INSERT INTO avisos (Mensajes, id_productos, id_usuario, nombre_producto) VALUES (%s, %s, %s, %s)",
            (mensaje, id, id_usuario, nombre_producto)
        )
        conexion.commit()
        return True
    except:
        return False
















def mensajes(id_usuario):
    try:
        cursor.execute("select * from avisos where id_usuario=%s", (id_usuario,))
        mensajes = cursor.fetchall()
        return mensajes
    except:
        return False















    try:
        cursor.execute("update notas set titulo=%s, descripcion=%s, fecha=NOW() where id=%s",(titulo,descripcion,id))
        conexion.commit()
        return True
    except:
        return False
