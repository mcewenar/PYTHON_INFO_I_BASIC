Proceso mantenimiento_equipos
	Definir area,equipo_biomedico, equipo_computo,equipo_infraestructura Como Caracter;
	Definir a como entero;
	area<-"";
	equipo_biomedico<-"";
	equipo_computo<-"";
	equipo_infraestructura<-"";
	a<-0;
	Escribir "Ingrese el tipo de equipo que requiere ser reportado, si es equipo biomédico ingrese (1), si es equipo de computo ingrese (2) si es equipo de infraestructura ingrese(3)";
	leer a;
	si a==1 entonces;
		Escribir "Su solicitud ha sido enviada al Ingeniero Biomédico del hospital";
	SiNo
		si a==2 entonces
			Escribir "Su solicitud ha sido enviada al Ingeniero de sistemas del hospital";
		SiNo
			si a==3 entonces;
				Escribir "Su solicitud ha sido enviada al coordinador de infraestructura del hospital";
			SiNo
				Escribir "Opción incorrecta";
			FinSi
		FinSi
	FinSi
FinProceso
