#Unas pocas palabras acerca de None (IMPORTANTE)

#Permítenos presentarte un valor muy curioso (para ser honestos, un valor que es ninguno) llamado None.

#Sus datos no representan valor razonable alguno; en realidad, no es un valor en lo absoluto; por lo tanto, no debe participar en 
# ninguna expresión.

#Por ejemplo, un fragmento de código como el siguiente:

#print(None + 2)
#Causará un error de tiempo de ejecución, descrito por el siguiente mensaje de diagnóstico:
#TypeError: unsupported operand type(s) for +: 'NoneType' and 'int'

#Nota: None es una palabra reservada.

#IMPORTANTE:
#Solo hay dos tipos de circunstancias en las que None se puede usar de manera segura:
#Cuando se le asigna a una variable (o se devuelve como el resultado de una función).
#Cuando se compara con una variable para diagnosticar su estado interno.
#Al igual que aquí:
valor = None
if valor == None:
    print("Lo siento, no tienes ningún valor") 


#IMPORTANTE:
#No olvides esto: si una función no devuelve un cierto valor utilizando una cláusula de expresión return, se asume que devuelve 
# implícitamente None.

#Vamos a probarlo.

print("-------2--------")
def noneFunct(a,b):
    a + b
    return #DEVUELVE NONE SI NO HAY UNA EXPRESIÓN QUE LA SIGA

x=noneFunct(3,3)
print(x)
#Salida: None.



def noneFunct(a,b):
    c = a + b
    return c #DEVUELVE NONE SI NO HAY UNA EXPRESIÓN QUE LA SIGA

x=noneFunct(3,3)
print(x)
#Salida: 6



print("------3------")

#Algunas palabras acerca de None: continuación
#Echa un vistazo al código en el editor.

def strangeFunction(n):
    if(n % 2 == 0):
        return True
    #cuando no entra a un if, regresa None (o así tuviese un return solamente)
#Es obvio que la función strangeFunction devuelve True cuando su argumento es par.

#¿Qué es lo que regresa de otra manera?

#Podemos usar el siguiente código para verificarlo:

print(strangeFunction(2))
print(strangeFunction(1)) 