Proceso sueldos
	Definir d, s como Real;
	d<-0; s<-0;
	Escribir  "Por favor ingrese su sueldo";
	Leer s;
	Si s<800000 Entonces
		d<-s*0.10;
		s<-s-d;
	SiNo
		si 1000000<s y s<2000000 entonces
			d<-s*0.05;
			s<-s-d;
		SiNo
			si s>=2000000 entonces
				d<-s*0.03;
				s<-s-d;
				
			FinSi
		FinSi
	FinSi
	Escribir "Su descuento fue de ", d, " y su salario equivale a ", s;
FinProceso
