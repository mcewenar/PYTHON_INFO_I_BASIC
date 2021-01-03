Proceso val_medio
	Definir a, b, c, val_central como Real;
	Definir k como Caracter;
	
	a<-0;
	b<-0;
	c<-0;
	val_central<-0;
	k<-"S";
	Mientras k == "S" hacer
	Escribir "Ingrese los 3 valores que desea comparar";
	Leer a;
	Leer b;
	Leer c;
		Si a<b y b<c entonces
		val_central<-b;
			Escribir "El valor central es: ", val_central;
		SiNo
			si c<b y b<a entonces
				al_central<-b;
				Escribir "El valor central es: ", val_central;
			FinSi
		FinSi	
		si b<a y a<c Entonces
			val_central<-a;
			Escribir "El valor central es: ", val_central;
		SiNo
			Si c<a y a<b Entonces
				val_central<-a;
				Escribir "El valor central es: ", val_central;
			FinSi
		FinSi
		Si a<c y c<b Entonces
			val_central<-c;
			Escribir "El valor central es: ", val_central;
		SiNo
			Si b<c y c<a entonces
				val_central<-c;
				Escribir "El valor central es: ", val_central;
			FinSi
		FinSi
		Si a==b o b==c Entonces
			Escribir "No hay valor central, pues hay dos o más valores identicos";
		
		FinSi
	a<-0;
	b<-0;
	c<-0;
	val_central<-0;
	Escribir "Desea ingresar 3 valores nuevos? Si lo desea ingrese S";
	Leer k;
	FinMientras
	Escribir "Ha finalizado su proceso";
	
		
FinProceso
