Proceso potencias_de_3
	definir i,j, m Como Real;
	i<-0;
	j<-0;
	m<-0;
	Mientras i<30 hacer 
		j<-3^i;
		Escribir j;
		m<-m+j;
		i<-i+1;
	FinMientras
	Escribir "La suma de las 30 primeras potencias de 3= ",m;
	
FinProceso
