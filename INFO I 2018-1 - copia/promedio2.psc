Proceso promedio2
	Definir N, M, i, a, suma Como Entero;
	Definir promedio Como Real;
	Definir b Como Caracter;
	M<-0; i<-0; a<-0; suma<-0; N<--100;
	b<-"S";
	Mientras b == "S" Hacer
		Escribir "Ingrese desde qué valor de N desea realizar el promedio";
		Leer M;
		Para a<-N Hasta M con paso 1 Hacer
			i<-a+1;
			suma<-suma+i;
		FinPara 
		Escribir "El promedio es: ", suma/abs(M-N);
		N<-0; i<-0; a<-0; suma<-0;
		Escribir "Si desea realizar el proceso nuevamente, ingrese S";
		Leer b;
	FinMientras
	Escribir "Ha finalizado su proceso";
	
FinProceso
