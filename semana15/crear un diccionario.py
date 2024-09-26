# Crear un diccionario llamado informacion_personal
informacion_personal = {
 "nombre": "Carlos Pérez",
 "edad": 30,
 "ciudad": "Quito",
 "profesion": "Ingeniero"
}
# Acceder y modificar el valor de la clave "ciudad"
informacion_personal["ciudad"] = "Guayaquil"
# Agregar una nueva clave-valor para "profesion"
informacion_personal["profesion"] = "Desarrollador de software"
# Verificar si la clave "telefono" existe y agregarla si no existe
if "telefono" not in informacion_personal:
 informacion_personal["telefono"] = "0987654321"
# Eliminar la clave "edad" del diccionario
del informacion_personal["edad"]
# Imprimir el diccionario resultante
print(informacion_personal)