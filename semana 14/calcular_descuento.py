#calcular los descuentos
#descuento del 10%

def calcular_descuento(monto_total, porcentaje_descuento=10):
    """
    Calcula el monto del descuento dado un monto total y un porcentaje de descuento.

    :param monto_total: El monto total de la compra.
    :param porcentaje_descuento: El porcentaje de descuento (por defecto 10%).
    :return: El monto del descuento calculado.
    """
    descuento = monto_total * (porcentaje_descuento / 100)
    return descuento

# Llamada a la función con solo el monto total
monto_total1 = 200
descuento1 = calcular_descuento(monto_total1)
monto_final1 = monto_total1 - descuento1
print(f"Compra de ${monto_total1}: Descuento = ${descuento1:.2f}, Monto final = ${monto_final1:.2f}")

# Llamada a la función con monto total y porcentaje de descuento
monto_total2 = 300
porcentaje_descuento2 = 15
descuento2 = calcular_descuento(monto_total2, porcentaje_descuento2)
monto_final2 = monto_total2 - descuento2
print(f"Compra de ${monto_total2} con un descuento del {porcentaje_descuento2}%: Descuento = ${descuento2:.2f}, Monto final = ${monto_final2:.2f}")

