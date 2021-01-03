Proceso sin_titulo
	Definir HCE, p, nombre, apellido, genero, codigo, EPS Como Caracter;
	Definir i, j, regimen, paciente como Entero;
	Definir ID como Real;
	Dimension HCE[100,6];
	i<-0; j<-0; p<-"1"; codigo<-""; regimen<-0; paciente<-0; 
	
	Mientras p=="1" hacer
		paciente<-paciente+1;
		Para i<-paciente hasta paciente con paso 1 hacer
			Escribir ("Por favor ingrese el nombre del paciente");
			Leer HCE[i,0];
			Escribir ("Ingrese por favor el apellido");
			Leer HCE[i,1];
			Escribir ("Ingrese por favor el ID");
			Leer HCE[i,2];
			Escribir ("Ingrese por favor el género");
			Leer HCE[i,3];
			Escribir "Ingrese por favor el régimen al que pertenece. Si es subsidiado, es decir SISBEN, ingrese 1. Si es contributivo, es decir tiene EPS, ingrese 2";
			Leer regimen;
			Si regimen=1 entonces
				HCE[i,4]<-"sisben";
				codigo<-"HCE-"+HCE[i,4]+"-"+ConvertirATexto(paciente);
				HCE[i,5]<-codigo;
			SiNo
				Si regimen=2 entonces
					Escribir "Qué EPS tiene?";
					Leer EPS;
					HCE[i,4]<-EPS;
					codigo<-"HCE-"+HCE[i,4]+"-"+ConvertirATexto(paciente);
					HCE[i,5]<-codigo;
				FinSi
			FinSi
		FinPara
		Escribir "Desea ingresar una nueva historia clínica? Si su respuesta es Sí, ingrese 1. Si su respuesta es no, ingrese 2";
		Leer p;
	FinMientras
	Para i<-1 hasta paciente con paso 1 hacer
		Escribir "Información del paciente # ", i;
		PARA j<-0 hasta 5 con paso 1 hacer
			Escribir HCE[i,j];
		FinPara
		Escribir " ";
	FinPara
	Escribir "Ha finalizado el proceso";
	
FinProceso
