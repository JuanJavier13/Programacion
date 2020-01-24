Algoritmo TablaMultiplicacion
	data <- 0
	Mientras data<1 O data>12 Hacer
		Escribir 'Insertar un numero del 1 al 12: '
		Leer data
		Si data<=0 Entonces
			Escribir 'Error el valor debe ser mayor que 0'
		SiNo
			Si data>12 Entonces
				Escribir 'Error el valor de ser menor que 12'
			FinSi
		FinSi
	FinMientras
	min <- 1
	max <- 12
	Mientras min<=max Hacer
		Escribir data,'*',min,'=',data*min
		min <- min+1
	FinMientras
	acumulador = data * 78
	Escribir data * 78
FinAlgoritmo
