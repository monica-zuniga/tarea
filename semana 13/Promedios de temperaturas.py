#calcular la temperatura promedio de tres cuidades
#ciudades: Riobamba, Macas y Guayaquil

def calcular_temperatura_promedio_ciudades(datos_temperaturas):
    """
    Calcula la temperatura promedio para cada ciudad durante el periodo dado.

    :param datos_temperaturas: Diccionario donde las claves son nombres de ciudades y los valores son listas de listas
                               con temperaturas semanales.
    :return: Diccionario con las ciudades y sus temperaturas promedio.
    """
    promedios = {}

    for ciudad, semanas in datos_temperaturas.items():
        todas_las_temperaturas = [temp for semana in semanas for temp in semana]
        if todas_las_temperaturas:  # Verifica que la lista de temperaturas no esté vacía
            promedio = sum(todas_las_temperaturas) / len(todas_las_temperaturas)
        else:
            promedio = None  # O puedes usar 0 o alguna otra forma de manejar listas vacías

        promedios[ciudad] = promedio

    return promedios


# Ejemplo de uso
datos_temperaturas = {
    "Ríobamba": [
        [69, 72, 47, 65, 63, 66, 64],  # Semana 1
        [62, 65, 67, 68, 68, 67, 67],  # Semana 2
        [66, 65, 65, 65, 65, 66, 69],  # Semana 3
        [70, 70, 70, 66, 65, 65, 65]  # Semana 4
    ],
    "Macas": [
        [93, 94, 91, 92, 92, 92, 91],  # Semana 1
        [91, 92, 92, 92, 91, 91, 92],  # Semana 2
        [93, 92, 92, 92, 92, 91, 90],  # Semana 3
        [93, 92, 91, 91, 92, 90, 90]  # Semana 4
    ],
    "Guayaquil": [
        [89, 90, 68, 89, 88, 88, 90],  # Semana 1
        [90, 89, 90, 90, 90, 90, 90],  # Semana 2
        [89, 89, 90, 92, 89, 89, 89],  # Semana 3
        [89, 90, 91, 89, 90, 90, 90]  # Semana 4
    ]
}

resultados = calcular_temperatura_promedio_ciudades(datos_temperaturas)
print(resultados)
