Proceso num_central
	Definir a,b,c,central Como Real;
	a<-0;
	b<-0;
	c<-0;
	central<-0;
	Escribir "Ingrese el primer número";
	Leer a;
	Escribir "Ingrese el segundo número";
	Leer b;
	Escribir "Ingrese el tercer número";
	Leer c;
	si (a>b) y (b>c) Entonces
		central<-b;
	FinSi
	si (c>b) y (b>a) Entonces
		central<-b;
	FinSi
	
	si (b>a) y (a>c) Entonces
		central<-a;
	FinSi
	
	si (c>a) y (a>b) Entonces
		central<-a;
	Finsi
	si (a>c) y (c>b) Entonces
		central<-c;
	finsi
	si (b>c) y (c>a) entonces
		central<-c;
	finsi
	
	Escribir  central;
FinProceso
