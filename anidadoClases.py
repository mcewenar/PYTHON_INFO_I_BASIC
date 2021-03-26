#Herencia: issubclass()

#Python ofrece una función que es capaz de identificar una relación entre dos clases, y aunque su diagnóstico no es complejo, 
#puede verificar si una clase particular es una subclase de cualquier otra clase.

#Así es como se ve:

#issubclass(ClaseUno, ClaseDos) True si ClaseUno es subclase de ClaseDos

#La función devuelve True si ClaseUno es una subclase de ClaseDos, y False de lo contrario.

#Vamos a verlo en acción, puede sorprenderte. Mira el código en el editor. Léelo cuidadosamente.
class Vehiculo:
    pass

class VehiculoTerrestre(Vehiculo):
    pass

class VehiculoOruga(VehiculoTerrestre):
    pass


for cls1 in [Vehiculo, VehiculoTerrestre, VehiculoOruga]:
    for cls2 in [Vehiculo, VehiculoTerrestre, VehiculoOruga]:
        print(issubclass(cls1, cls2), end="\t")
    print()

#Hay dos bucles anidados. Su propósito es verificar todos los pares de clases ordenadas posibles y que imprima los resultados de la 
#verificación para determinar si el par coincide con la relación subclase-superclase.

#Ejecuta el código. El programa produce el siguiente resultado:

#True	False	False	
#True	True	False	
#True	True	True	

#Hagamos que el resultado sea más legible:

#↓ es una subclase de →	Vehiculo	VehiculoTerrestre	VehiculoOruga
#Vehiculo	True	False	False
#VehiculoTerrestre	True	True	False
#VehiculoOruga	True	True	True
#Existe una observación importante que hacer: cada clase se considera una subclase de sí misma.
