#calcular_temperatura_promedio_cuidades
#cuidades:Riobamba,Macas,Guayaquil

def calcular_temperaturas_promedio_cuidades(temperaturas_semanales):
    """calcula_la_temperatura_promedio_para_cada_ciudad_durante_el_periodo_dado.
    :param
    temperaturas_semanales:diccionario donde las claves son nombres de cuidades
    y los valores son listas de listas
    con temperaturas semanales.
    return:Diccionario con las cuidades y sus temperaturas promedio"""
        promedios = {}

    for cuidad, semanas in temperaturas_semanales.items():
        todas_las_temperaturas =

        [temp for semans in semanas for temp in semana]
        if
todas_las_temperaturas:
#Verificar que la lista de temperatura no este vacía
[69,72,47,65,63,66,64],[62,65,67,68,68,67,67],
[66,65,65,65,65,66,69],[70,70,70,66,65,65,65],
[93,94,91,92,92,92,91],[91,92,92,92,91,91,92],
[93,92,92,92,92,91,90],[93,92,91,91,92,90,90],
[89,88,68,89,88,88,90],[90,89,90,90,90,90,90],
[89,89,90,92,89,89,89],[88,90,91,89,90,90,90]

            promedio =
            sum(ttodas las temperaturas) /
            len(todas_las_temperaturas)
        else:
            promedio = None
#o puedes usar 0 o alguna otra forma de manejar listas vacias
                        promedios[cuidades] = promedio
            return promedios

        datos_temperaturas =
{"Riobamba": [[69,72,47,65,63,66,64],[62,65,67,68,68,67,67],
[66,65,65,65,65,66,69],[70,70,70,66,65,65,65]],
"Macas": [[93,94,91,92,92,92,91],[91,92,92,92,91,91,92],
[93,92,92,92,92,91,90],[93,92,91,91,92,90,90]],
"Guayaquil": [[89,88,68,89,88,88,90],[90,89,90,90,90,90,90],
[89,89,90,92,89,89,89],[88,90,91,89,90,90,90]]}

        resultados =
        calcular_temperatura_promedio_ciudades(datos_temperaturas)
        print(resultados)










