Proceso suma_multiplos_de_3
	Definir i,j Como Entero;
	i<-0;
	j<-0;
	mientras i<10 hacer 
		si i%3==0 Entonces
			j<-j+i;
		FinSi
		i<-i+1;
		escribir i;
		
	FinMientras
	escribir "la sumatoria de los multiplos de 3 es = ",j;
	
FinProceso
