# Sintaxis condicionales

# if condicion:
#     instrucciones si la condicion es verdadera
#  elif condicion: 
#      instrucciones si la otra condicion es verdadera
# else
#      instrucciones si ninguna condicion es verdadera

# Ejercicio 1: Programa que pide un número y muestre si es positivo, negativo o cero
numero = float(input("Ingrese un número"))

if número > 0: 
   print("Bloque if ejecutado.")
   print("El número es negativo.")
elif numero < 0:
   print("Bloque elif ejecutado.")
   print("El número es negativo.")
else:
   print("Bloque else ejecutado.")
   print("El número es cero.")

print(¨----------------¨)

# if condicion
#     if 




# Ejercicio 2: Programa que pida dos números y muestre cuál es mayor o si son iguales

num1 = float(input)











# Ejercicio 3: Haz un programa que pida una calificación del 0 al 10 y muestre si está aprobado o reprobado. Toma en cuenta una calificación del 0 al 10 y muestre si está aprobado o reprobado. Toma en cuenta una calificación mayor o igual a 6 como aprobatoria

nombreAlumno = input("Ingrese el nombre del alumno: ")
calificacion = float(input("Ingrese la calificación del alumno (0 - 10):"))

if calificacion >= 6:
   print(f"El alumno {nombreAlumno}está aprobado.")
else:
    print(f"El alumno {nombreAlumno}está reprobado.")

    print("--------------")

    # Ejercicio 4: Haz un programa que pida la edad de una persona y muestre si puede votar(mayor o igual a 18 años) o no

    nombre = input("Ingrese el nombre de la persona: ")
    edadPersona = int(input("Ingrese su edad."))

if edadPersona >=18:
   print(f"{nombre}") tiene {edadPersona} años y puede votar.")
else:
   print(f"{nombre}") tiene {edadPersona} años y no puede votar.")
