Proceso promedio_estudiantes
	Definir i, j, n1, n2, n3, n4, n5, d, c, promedio como Real;
	Dimension promedio[6];
	i<-0; j<-0; n1<-0; n2<-0; n3<-0; n4<-0; n5<-0; c<-0; 
	mientras c<6 Hacer
		promedio[c]<-0;
		c<-c+1;
		
	FinMientras
	
	Mientras i<5 Hacer
		
		Escribir "Alumno ", i, " ingrese sus notas en orden";
		Leer n1;
		Leer n2;
		Leer n3;
		Leer n4;
		Leer n5;
		d<-(n1+n2+n3+n4+n5)/5;
		i<-i+1;
		promedio[i]<-d;
		Si promedio[i]>=3 entonces 
			Escribir "Promedio del estudiante ", i-1, " es: ", promedio[i];
		SiNo
			Si promedio[i]<3 Entonces
				Escribir "Apreciado estudiante, usted ha reprobado la materia en una nota de ", promedio[i];
			FinSi
			
		FinSi
	FinMientras
	
	
FinProceso
