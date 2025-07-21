
def conectar():
    import mysql.connector
    conexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="bd_peliculas"
)
    

    if conexion.is_connected():
        print("✅ Conexión exitosa a la base de datos")
        conexion.close()
        
        return conexion
