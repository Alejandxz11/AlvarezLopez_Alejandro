# Pide una cantidad de productos y su precio uno por uno, luego muestra el total con IVA del 16%.

cantidad = int(input("¿Cuántos productos vas a ingresar?: "))
subtotal = 0.0
i = 1
while i <= cantidad:
    entrada = input("Precio del producto {}: ".format(i))
    try:
        precio = float(entrada.replace(',', '.'))
        if precio < 0:
            print("Precio no puede ser negativo. Intenta de nuevo.")
            continue
    except ValueError:
        print("Entrada inválida. Usa números, por ejemplo 12.50")
        continue
    subtotal += precio
    i += 1
iva = subtotal * 0.16
total = subtotal + iva
print("Subtotal:", round(subtotal, 2))
print("IVA (16%):", round(iva, 2))
print("Total con IVA:", round(total, 2))