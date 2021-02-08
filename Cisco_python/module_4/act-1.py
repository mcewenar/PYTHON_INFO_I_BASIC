#Tu tarea es escribir y probar una función que toma un argumento (un año) y devuelve True si el año es un año bisiesto, 
#o False sí no lo es.
#Parte del esqueleto de la función ya está en el editor.
#Nota: también hemos preparado un breve código de prueba, que puedes utilizar para probar tu función.

#El código utiliza dos listas: una con los datos de prueba y la otra con los resultados esperados. 
#El código te dirá si alguno de tus resultados no es válido.

    


def isYearLeap(year):
    #FORMA COMPACTA
    if testData[i] % 4 == 0 and (testData[i] % 100 != 0 or testData[i] % 400 == 0):
	    return True
    else:
	    return False

    #FORMA NO COMPACTA
    #if testData[i]%4!=0:
    #    return False
    #elif testData[i]%100!=0:
    #    return True
    #elif testData[i]%400!=0:
    #    return False
    #else: 
    #    return True
    

testData = [1900, 2000, 2016, 1987]
testResults = [False, True, True, False] #NO SON BISIESTOS 1900 NI 1987
for i in range(len(testData)):
	yr = testData[i]
	print(yr,"->",end="")
	result = isYearLeap(yr)
	if result == testResults[i]:
		print("OK")
	else:
		print("Error")
