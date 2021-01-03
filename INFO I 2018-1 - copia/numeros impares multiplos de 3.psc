Proceso num_impares_multiplos_de_3
	Definir i, b, N Como Entero;
	i<-0; b<-0; N<-0;
	Escribir "Ingrese el numero desde el cual desea hacer el analisis";
	Leer N;
	Mientras i<5 hacer
		si N%2==1 Entonces
			N<-N+2;
			
			Escribir N;
		FinSi
		i<-i+1;
		si N%3==0 entonces
			b<-N;
			
		FinSi
	FinMientras
	Escribir "numeros impares multiplos de 3: ", b;
FinProceso
