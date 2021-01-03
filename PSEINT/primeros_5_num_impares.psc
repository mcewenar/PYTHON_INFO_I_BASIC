Proceso primeros_5_num_impares
	Definir i, N Como Entero;
	i<-0; N<-0;
	Escribir "Ingrese el numero desde el cual desea hacer el analisis";
	Leer N;
	Mientras i<5 hacer
		si N%2==1 Entonces
			N<-N+2;
			Escribir N;
		
		SiNo
			si N%2==0 entonces
				N<-N+1;
				Escribir N;
			FinSi
		FinSi

		i<-i+1;	
	FinMientras
		
FinProceso
