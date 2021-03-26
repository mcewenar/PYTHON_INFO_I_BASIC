#Variables de instancia: continuación
#Observa el ejemplo modificado en el editor.

#Es casi lo mismo que el anterior. La única diferencia está en los nombres de las propiedades. 
#Hemos agregado dos guiones bajos (__) en frente de ellos.

#Como sabes, tal adición hace que la variable de instancia sea privada - se vuelve inaccesible desde el mundo exterior.

#El comportamiento real de estos nombres es un poco más complicado, así que ejecutemos el programa. Esta es la salida:

class ClaseEjemplo:
    def __init__(self, val = 1):
        self.__primera = val

    def setSegunda(self, val):
        self.__segunda = val


objetoEjemplo1 = ClaseEjemplo()
objetoEjemplo2 = ClaseEjemplo(2)

objetoEjemplo2.setSegunda(3)

objetoEjemplo3 = ClaseEjemplo(4)
objetoEjemplo3.__tercera = 5


print(objetoEjemplo1.__dict__)
print(objetoEjemplo2.__dict__)
print(objetoEjemplo3.__dict__)

#Salida:
#{'_ClaseEjemplo__primera': 1}
#{'_ClaseEjemplo__primera': 2, '_ClaseEjemplo__segunda': 3}
#{'_ClaseEjemplo__primera': 4, '__tercera': 5}

#¿Puedes ver estos nombres extraños llenos de guiones bajos? ¿De dónde provienen?

#Cuando Python ve que deseas agregar una variable de instancia a un objeto y lo vas a hacer dentro de cualquiera de los métodos del objeto, 
#maneja la operación de la siguiente manera:

#Coloca un nombre de clase antes de tu nombre.
#Coloca un guión bajo adicional al principio.
#Es por ello que __primera se convierte en _ClaseEjemplo__primera.

#El nombre ahora es completamente accesible desde fuera de la clase. Puedes ejecutar un código como este:

print(objetoEjemplo1._ClaseEjemplo__primera)

#y obtendrás un resultado válido sin errores ni excepciones.

#Como puedes ver, hacer que una propiedad sea privada es limitado.

#No funcionará si agregas una variable de instancia fuera del código de clase. En este caso, 
#se comportará como cualquier otra propiedad ordinaria.

print("---2---")

#Variables de Clase
#Una variable de clase es una propiedad que existe en una sola copia y se almacena fuera de cualquier objeto.

#Nota: no existe una variable de instancia si no hay ningún objeto en la clase; existe una variable de clase en una copia,
#incluso si no hay objetos en la clase.

#Las variables de clase se crean de manera diferente. El ejemplo te dirá más:

class ClaseEjemplo:
    contador = 0 #Variable de clase
    def __init__(self, val = 1):
        self.__primera = val
        ClaseEjemplo.contador += 1 #CUENTA TODOS LOS OBJETOS CREADOS 

objetoEjemplo1 = ClaseEjemplo()
objetoEjemplo2 = ClaseEjemplo(2)
objetoEjemplo3 = ClaseEjemplo(4)

print(objetoEjemplo1.__dict__, objetoEjemplo1.contador)
print(objetoEjemplo2.__dict__, objetoEjemplo2.contador)
print(objetoEjemplo3.__dict__, objetoEjemplo3.contador)


#Observa:

#Hay una asignación en la primera linea de la definición de clase: establece la variable denominada contador a 0;
#inicializando la variable dentro de la clase pero fuera de cualquiera de sus métodos hace que la variable sea una variable de clase.
#El acceder a dicha variable tiene el mismo aspecto que acceder a cualquier atributo de instancia; está en el cuerpo del constructor;
#como puedes ver, el constructor incrementa la variable en uno; en efecto, la variable cuenta todos los objetos creados.
#Ejecutar el código causará el siguiente resultado:

#{'_ClaseEjemplo__primera': 1} 3
#{'_ClaseEjemplo__primera': 2} 3
#{'_ClaseEjemplo__primera': 4} 3

#Dos conclusiones importantes provienen del ejemplo:

#Las variables de clase no se muestran en el diccionario de un objeto __dict__ (esto es natural ya que las variables de clase 
#no son partes de un objeto), 
#pero siempre puedes intentar buscar en la variable del mismo nombre, pero a nivel de clase, te mostraremos esto muy pronto.
#Una variable de clase siempre presenta el mismo valor en todas las instancias de clase (objetos).

print("---3---")

#Variables de Clase: continuación
#Mira el ejemplo en el editor. ¿Puedes adivinar su salida?

#Ejecuta el programa y verifica si tus predicciones fueron correctas. Todo funciona como se esperaba, ¿no? Funciona igual.

class ClaseEjemplo:
    __contador = 0
    def __init__(self, val = 1):
        self.__primera = val
        ClaseEjemplo.__contador += 1

objetoEjemplo1 = ClaseEjemplo()
objetoEjemplo2 = ClaseEjemplo(2)
objetoEjemplo3 = ClaseEjemplo(4)
    
print(objetoEjemplo1.__dict__, objetoEjemplo1._ClaseEjemplo__contador)
print(objetoEjemplo2.__dict__, objetoEjemplo2._ClaseEjemplo__contador)
print(objetoEjemplo3.__dict__, objetoEjemplo3._ClaseEjemplo__contador)


print("---4---")
#Importante:
#Variables de Clase: continuación
#Hemos dicho antes que las variables de clase existen incluso cuando no se creó ninguna instancia de clase (objeto).

#Ahora aprovecharemos la oportunidad para mostrarte la diferencia entre estas dos variables __dict__, la de la clase y la del objeto.

#Observa el código en el editor. La prueba está ahí.
class ClaseEjemplo:
    varia = 1
    def __init__(self, val):
        ClaseEjemplo.varia = val

print(ClaseEjemplo.__dict__)
objetoEjemplo = ClaseEjemplo(2)

print(ClaseEjemplo.__dict__) #Lleno de cosas
print(objetoEjemplo.__dict__) #Vacío

#Echemos un vistazo más de cerca:

#Definimos una clase llamada ClaseEjemplo.
#La clase define una variable de clase llamada varia.
#El constructor de la clase establece la variable con el valor del parámetro.
#Nombrar la variable es el aspecto más importante del ejemplo porque:
#El cambiar la asignación a self.varia = val crearía una variable de instancia con el mismo nombre que la clase.
#El cambiar la asignación a varia = val operaría en la variable local de un método; (te recomendamos probar los dos casos anteriores; 
#esto te facilitará recordar la diferencia).
#La primera línea del código fuera de la clase imprime el valor del atributo ClaseEjemplo.varia. Nota: 
#utilizamos el valor antes de instanciar el primer objeto de la clase.
#Ejecuta el código en el editor y verifica su salida.

#Como puedes ver __dict__ contiene muchos más datos que la contraparte de su objeto. 
#La mayoría de ellos son inútiles ahora - el que queremos que verifiques cuidadosamente muestra el valor actual de varia.

#Nota que el __dict__ del objeto está vacío - el objeto no tiene variables de instancia.

print("---5---")
#Comprobando la existencia de un atributo
#La actitud de Python hacia la instanciación de objetos plantea una cuestión importante: en contraste con otros lenguajes de programación, 
#es posible que no esperes que todos los objetos de la misma clase tengan los mismos conjuntos de propiedades.

#Justo como en el ejemplo en el editor. Míralo cuidadosamente.
class ClaseEjemplo:
    def __init__(self, val):
        if val % 2 != 0:
            self.a = 1 #atrobutos
        else:
            self.b = 1

objetoEjemplo = ClaseEjemplo(1)

print(objetoEjemplo.a)
#print(objetoEjemplo.b) GENERA ERROR

#El objeto creado por el constructor solo puede tener uno de los dos atributos posibles: a o b.

#La ejecución del código producirá el siguiente resultado:
#Salida:
#1
#Traceback (most recent call last):
#  File ".main.py", line 11, in 
#    print(objetoEjemplo.b)
#AttributeError: 'ClaseEjemplo' object has no attribute 'b'

#Como puedes ver, acceder a un atributo de objeto (clase) no existente provoca una excepción AttributeError.

print("----6----")

#Comprobando la existencia de un atributo: continuación
#La instrucción try-except te brinda la oportunidad de evitar problemas con propiedades inexistentes.

#Es fácil: mira el código en el editor.

#NO  ES UNA BUENA FORMA DE EVITAR ERRORES
class ClaseEjemplo:
    def __init__(self, val):
        if val % 2 != 0:
            self.a = 1
        else:
            self.b = 1

objetoEjemplo = ClaseEjemplo(1)
print(objetoEjemplo.a)

try:
    print(objetoEjemplo.b)
except AttributeError:
    pass

#Como puedes ver, esta acción no es muy sofisticada. Esencialmente, acabamos de barrer el tema debajo de la alfombra.

#Afortunadamente, hay una forma más de hacer frente al problema.

#IMPORTANTE:
#Python proporciona una función que puede verificar con seguridad si algún objeto / clase contiene una propiedad específica. 
#La función se llama hasattr, y espera que le pasen dos argumentos:

#La clase o el objeto que se verifica.
#El nombre de la propiedad cuya existencia se debe informar (Nota: debe ser una cadena que contenga el nombre del atributo).
#La función retorna True o False.

#Así es como puedes utilizarla:

class ClaseEjemplo:
    def __init__(self, val):
        if val % 2 != 0:
            self.a = 1
        else:
            self.b = 1

objetoEjemplo = ClaseEjemplo(1)
print(objetoEjemplo.a)

if hasattr(objetoEjemplo, 'b'):
    print(objetoEjemplo.b)





