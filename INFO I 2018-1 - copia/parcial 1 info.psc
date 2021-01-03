Proceso promedio_desde_N
	
	Definir N, acumulador, a, suma Como Entero;
	Definir promedio Como Real;
	Definir b Como Caracter;
	N<-0; acumulador<-0; a<-0; suma<-0; 
	b<-"S";
	Mientras b == "S" Hacer
		Escribir "Ingrese desde qué valor de N desea realizar el promedio";
		Leer N;
		Para a<-N Hasta N+98 con paso 1 Hacer
			acumulador<-acumulador+1;
			suma<-suma+N+acumulador;
		FinPara 
		Escribir "El promedio es: ", suma/100;
		N<-0; acumulador<-0; a<-0; suma<-0;
		Escribir "Si desea realizar el proceso nuevamente, ingrese S";
		Leer b;
	FinMientras
	Escribir "Ha finalizado su proceso";
FinProceso
