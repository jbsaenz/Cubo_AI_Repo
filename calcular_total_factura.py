def calcular_total_factura(cantidad_sin_iva, porcentaje_iva=21):
    total = cantidad_sin_iva * (1 + porcentaje_iva / 100)
    return total
