#Tu tarea es escribir y probar una función que toma dos argumentos (un año y un mes) y devuelve el número de días del mes/año dado 
#(mientras que solo febrero es sensible al valor year, tu función debería ser universal).
#La parte inicial de la función está lista. Ahora, haz que la función devuelva None si los argumentos no tienen sentido.
#Por supuesto, puedes (y debes) utilizar la función previamente escrita y probada (LAB 4.1.3.6). Puede ser muy útil. 
#Te recomendamos que utilices una lista con los meses. Puedea crearla dentro de la función; este truco acortará significativamente el código.
#Hemos preparado un código de prueba. Amplíalo para incluir más casos de prueba.


def isYearLeap(year):
	if year % 4 == 0 and (year%100 != 0 or year % 400 == 0):
		return True
	else:
		return False
def daysInMonth(year=None, month=None):
	if month in [1,3,5,7,8,10,12]:
		return 31
	elif month == 2:
		if isYearLeap(year):
   				return 29
		else:
    			return 28
	else:
		return 30

#FORMA MÁS LARGA
#def isYearLeap(year):
#	if testYears[i] % 4 == 0 and (testYears[i] % 100 != 0 or testYears[i] % 400 == 0):
#		return True
#	else:
#		return False

#def daysInMonth(year=None, month=None):
#	if testYears[i] % 4 == 0 and (testYears[i] % 100 != 0 or testYears[i] % 400 == 0) and testMonths[i] != 1:
#		return 29
#	elif testMonths[i]==1 or testMonths[i]==3 or testMonths[i]==5 or testMonths[i]==7 or testMonths[i]==8 or testMonths[i]==10 or testMonths[i]==12:
#		return 31
#	elif testMonths[i]==4 or testMonths[i]== 6 or testMonths[i]== 9 or testMonths[i]==11:
#		return 30
#	else:
#		return 28

testYears = [1900, 2000, 2016, 1987,1993]
testMonths = [2, 2, 1, 11,10]
testResults = [28, 29, 31, 30,31]
for i in range(len(testYears)):
	yr = testYears[i]
	mo = testMonths[i]
	print(yr, mo, "->", end="")
	result = daysInMonth(yr, mo)
	if result == testResults[i]:
		print("OK")
	else:
		print("Error")

