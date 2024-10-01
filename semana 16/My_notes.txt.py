# Escritura de Archivo de Texto

# Abre el archivo en modo de escritura ('w')
with open('my_notes.txt', 'w') as file:
    # Escribe tres líneas de notas personales
    file.write("Me gusta jugar futbol y soy fan de la seleccion ecuatoriana.\n")
    file.write("Mi comida favorita so los ceviches de chochos con cuero y arto aji.\n")
    file.write("Mis cansiones favoritas son los vallenatos y la que me encanta es vuelve.\n")

# Lectura de Archivo de Texto

# Abre el archivo en modo de lectura ('r')
with open('my_notes.txt', 'r') as file:
    # Lee el contenido línea por línea
    for line in file:
        # Muestra cada línea en la consola
        print(line.strip())  # .strip() elimina los saltos de línea extra

# El archivo se cierra automáticamente al usar 'with'.
