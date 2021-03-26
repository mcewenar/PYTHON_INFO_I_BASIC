#Comprobando la existencia de un atributo: continuación
#No olvides que la función hasattr() también puede operar en clases. Puedes usarlo para averiguar si una variable de clase está disponible, 
#como en el ejemplo en el editor.
class ClaseEjemplo:
    attr = 1

print(hasattr(ClaseEjemplo, 'attr'))
print(hasattr(ClaseEjemplo, 'prop'))
#Salida:
#True
#False

#La función devuelve True si la clase especificada contiene un atributo dado, y False de lo contrario.

#¿Puedes adivinar la salida del código? Ejecútalo para verificar tus conjeturas.


#Un ejemplo más: analiza el código a continuación e intenta predecir su salida:
print("---")
class ClaseEjemplo:
    a = 1 #Variable de clase
    def __init__(self):
        self.b = 2 #Atributo

objetoEjemplo = ClaseEjemplo()

print(hasattr(objetoEjemplo, 'b')) #Esta verifica si hay un atributos y a la vez variables de clase
print(hasattr(objetoEjemplo, 'a')) #igual acá
print(hasattr(ClaseEjemplo, 'b')) #estaopriedades revisa sólo variables de clase pero no atributos (pr)
print(hasattr(ClaseEjemplo, 'a'))

#¿Tuviste éxito? Ejecuta el código para verificar tus predicciones.
#Salida:
#True
#True
#False
#True

#Bien, hemos llegado al final de esta sección. En la siguiente sección vamos a hablar sobre los métodos, 
#ya que los métodos dirigen los objetos y los activan.