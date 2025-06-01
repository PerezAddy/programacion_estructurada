from paquete1 import modulos

print(modulos.saludar("Daniel Contreras Ruano"))

modulos.borrarPantalla()
nom,tel=modulos.solicitarDatos()
print(f".: Agenda Telefonica:  nombre: {nom}  telefono: {tel}" )
modulos.espereTecla()