Proceso suma_pares_e_impares
	definir a, b, j, i como Entero;
	a<-1; b<-0; i<-0; j<-0;
	
	Para a<-1 hasta a+49 con paso 1 Hacer
		si a%2==0 entonces
			i<-i+a;
			Escribir a;
		SiNo
			Si a%2==1 entonces
				j<-j+a;
				Escribir a;
			FinSi
		FinSi
		
	FinPara
	Escribir "La suma de los números pares entre 1 y 50 es: ", i;
	Escribir "La suma de los números impares entre 1 y 50 es: ", j;
		
FinProceso
