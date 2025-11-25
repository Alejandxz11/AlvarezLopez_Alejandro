#Funcion para ordenar estudiantes por promedio (de la calificación más alta a la más baja)

def ordenar_por_promedio(estudiantes):
	# estudiantes es una lista de diccionarios con 'nombre' y 'promedio'
	estudiantes_ordenados = sorted(estudiantes, key=lambda x: x['promedio'], reverse=True)
	return estudiantes_ordenados





 