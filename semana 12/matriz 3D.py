# Crear una matriz 3D para almacenar datos de temperaturas
# Primera dimensión: Ciudades (Riobamba,Macas,Guayaquil)
# Segunda dimensión: Semanas (4 semanas)
# Tercera dimensión: Días de la semana (7 días)
temperaturas = [
    [   # Ciudad de Riobamba
        [   # Semana 1
            {"day": "Lunes 2", "temp": 69},
            {"day": "Martes 3", "temp": 72},
            {"day": "Miércoles 4", "temp": 47},
            {"day": "Jueves 5", "temp": 65},
            {"day": "Viernes 6", "temp": 63},
            {"day": "Sábado 7", "temp": 66},
            {"day": "Domingo 8", "temp": 64}
        ],
        [   # Semana 2
            {"day": "Lunes 9", "temp": 62},
            {"day": "Martes 10", "temp": 65},
            {"day": "Miércoles 11", "temp": 67},
            {"day": "Jueves 12", "temp": 68},
            {"day": "Viernes 13", "temp": 68},
            {"day": "Sábado 14", "temp": 67},
            {"day": "Domingo 15", "temp": 67}
        ],
        [   # Semana 3
            {"day": "Lunes 16", "temp": 66},
            {"day": "Martes 17", "temp": 65},
            {"day": "Miércoles 18", "temp": 65},
            {"day": "Jueves 19", "temp": 65},
            {"day": "Viernes 20", "temp": 65},
            {"day": "Sábado 21", "temp": 66},
            {"day": "Domingo 22", "temp": 69}
        ],
        [   # Semana 4
            {"day": "Lunes 23", "temp": 70},
            {"day": "Martes 24", "temp": 70},
            {"day": "Miércoles 25", "temp": 70},
            {"day": "Jueves 26", "temp": 66},
            {"day": "Viernes 27", "temp": 65},
            {"day": "Sábado 28", "temp": 65},
            {"day": "Domingo 29", "temp": 65}
        ]
    ],
    [   # Ciudad de Macas
        [   # Semana 1
            {"day": "Lunes 2", "temp": 93},
            {"day": "Martes 3", "temp": 94},
            {"day": "Miércoles 4", "temp": 91},
            {"day": "Jueves 5", "temp": 92},
            {"day": "Viernes 6", "temp": 92},
            {"day": "Sábado 7", "temp": 92},
            {"day": "Domingo 8", "temp": 91}
        ],
        [   # Semana 2
            {"day": "Lunes 9", "temp": 91},
            {"day": "Martes 10", "temp": 92},
            {"day": "Miércoles 11", "temp": 92},
            {"day": "Jueves 12", "temp": 92},
            {"day": "Viernes 13", "temp": 91},
            {"day": "Sábado 14", "temp": 91},
            {"day": "Domingo 15", "temp": 92}
        ],
        [   # Semana 3
            {"day": "Lunes 16", "temp": 93},
            {"day": "Martes 17", "temp": 92},
            {"day": "Miércoles 18", "temp": 92},
            {"day": "Jueves 19", "temp": 92},
            {"day": "Viernes 20", "temp": 92},
            {"day": "Sábado 21", "temp": 91},
            {"day": "Domingo 22", "temp": 90}
        ],
        [   # Semana 4
            {"day": "Lunes 23", "temp": 93},
            {"day": "Martes 24", "temp": 92},
            {"day": "Miércoles 25", "temp": 91},
            {"day": "Jueves 26", "temp": 91},
            {"day": "Viernes 27", "temp": 92},
            {"day": "Sábado 28", "temp": 90},
            {"day": "Domingo 29", "temp": 90}
        ]
    ],
    [   # Ciudad de Guayaquil
        [   # Semana 1
            {"day": "Lunes 2", "temp": 89},
            {"day": "Martes 3", "temp": 88},
            {"day": "Miércoles 4", "temp": 68},
            {"day": "Jueves 5", "temp": 89},
            {"day": "Viernes 6", "temp": 88},
            {"day": "Sábado 7", "temp": 88},
            {"day": "Domingo 8", "temp": 90}
        ],
        [   # Semana 2
            {"day": "Lunes 9", "temp": 90},
            {"day": "Martes 10", "temp": 89},
            {"day": "Miércoles 11", "temp": 90},
            {"day": "Jueves 12", "temp": 90},
            {"day": "Viernes 13", "temp": 90},
            {"day": "Sábado 14", "temp": 90},
            {"day": "Domingo 15", "temp": 90}
        ],
        [   # Semana 3
            {"day": "Lunes 16", "temp": 89},
            {"day": "Martes 17", "temp": 89},
            {"day": "Miércoles 18", "temp": 90},
            {"day": "Jueves 19", "temp": 92},
            {"day": "Viernes 20", "temp": 89},
            {"day": "Sábado 21", "temp": 89},
            {"day": "Domingo 22", "temp": 89}
        ],
        [   # Semana 4
            {"day": "Lunes 23", "temp": 88},
            {"day": "Martes 24", "temp": 90},
            {"day": "Miércoles 25", "temp": 91},
            {"day": "Jueves 26", "temp": 89},
            {"day": "Viernes 27", "temp": 90},
            {"day": "Sábado 28", "temp": 90},
            {"day": "Domingo 29", "temp": 90}
        ]
    ]
]

# Calcular el promedio de temperaturas para cada ciudad y semana
for ciudad in temperaturas:
    for semana in ciudad:
        suma = 0
        for dia in semana:
            suma += dia['temp']
        print(suma)
