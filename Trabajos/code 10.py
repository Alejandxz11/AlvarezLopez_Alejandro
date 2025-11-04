#10Haz un programa que simule una calculadora básica con opciones de suma, resta, multiplicación y división, que se repita hasta que el usuario elija salir.

while True:
    print("----- Calculadora -----")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Salir")
    opcion = input("Elige una opción (1-5): ")
    if opcion == "5":
        print("Saliendo...")
        break
    if opcion in ("1", "2", "3", "4"):
        try:
            a = float(input("Ingresa el primer número: "))
            b = float(input("Ingresa el segundo número: "))
        except ValueError:
            print("Entrada inválida. Usa números, intenta de nuevo.")
            continue
        if opcion == "1":
            print("Resultado:", a + b)
        elif opcion == "2":
            print("Resultado:", a - b)
        elif opcion == "3":
            print("Resultado:", a * b)
        elif opcion == "4":
            if b == 0:
                print("Error: división por cero.")
            else:
                print("Resultado:", a / b)
    else:
        print("Opción inválida. Intenta de nuevo.")