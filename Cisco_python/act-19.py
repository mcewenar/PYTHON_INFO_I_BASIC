#Objetivos
#Familiarizarse con los conceptos de números, operadores y expresiones aritméticas en Python.
#Comprender la precedencia y asociatividad de los operadores de Python, así como el correcto uso de los paréntesis.
#Escenario
#La tarea es completar el código para poder evaluar la siguiente expresión:

#El resultado debe de ser asignado a y. Se cauteloso, observa los operadores y priorízalos. 
# Utiliza cuantos paréntesis sean necesarios.

#Puedes utilizar variables adicionales para acortar la expresión (sin embargo, no es muy necesario). 
# Prueba tu código cuidadosamente.

li=[1,10,100,-5]
for x in li:
    y=(1/(x+(1/(x+(1/(x+(1/x)))))))
    print("y= "+str(y))
    #o print("y=", y)
