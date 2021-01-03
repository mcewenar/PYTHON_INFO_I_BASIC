Proceso horas_trabajadas
	Definir e, n, h, s Como Real;
	e<-0; n<-0; s<-0;
	Escribir "Ingrese el valor de la hora laboral";
	Leer n;
	
	Escribir "Ingrese horas en la semana trabajadas";
	Leer h;
	Si h>54 Entonces
		e<-n+0.5*n;
		s<-h*n+(h-54)*e;
	sino
		si h<=54 Entonces
			s<-h*n;
		FinSi
	FinSi
	Escribir "el salario equivalente a la presente semana es: ", s;
	
FinProceso
