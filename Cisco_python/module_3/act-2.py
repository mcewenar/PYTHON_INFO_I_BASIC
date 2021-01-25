#Imagina que tu programa de computadora ama estas plantas. Cada vez que recibe una entrada en forma de la palabra 
#Espatifilo, grita involuntariamente a la consola la siguiente cadena:  "¡Espatifilo es la mejor planta de todas!" 

#Escribe un programa que utilice el concepto de ejecución condicional, tome una cadena como entrada y que:

#Imprima el enunciado "Si, ¡El Espatifilo es la mejor planta de todos los tiempos!"  en la pantalla si la cadena 
#ingresada es "Espatifilo".
#Imprima "No, ¡quiero un gran Espatifilo!" si la cadena ingresada es "espatifilo".
#Imprima  "¡Espatifilo! ¡No [entrada]!"  de lo contrario. Nota: [entrada] es la cadena que se toma como entrada.


planta=input("Enter the plant: ")

if planta=="Espatifilo":
    print("Sí, ¡el Espatifilo es la mejor planta de todos los tiempos!")
elif planta == "espatifilo":
    print("No, ¡quiero un gran Espatifilo!")
else:
    print("¡Espatifilo! ¡No "+planta+ "!")