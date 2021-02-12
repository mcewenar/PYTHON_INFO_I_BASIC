#Tu tarea es escribir y probar una función que toma tres argumentos (un año, un mes y un día del mes) 
#y devuelve el día correspondiente del año, o devuelve None si cualquiera de los argumentos no es válido.

#Debes utilizar las funciones previamente escritas y probadas. Agrega algunos casos de prueba al código. 
#Esta prueba es solo el comienzo.




def isYearLeap(year):
    if year % 4 == 0 and (year %100 != 0 or year % 400 == 0):
    	return True
    else:
	    return False

def daysInMonth(year, month):
	if month <= 0 or month > 12 or year < 1582:
    		return None
	else:
		if month in [1,3,5,7,8,10,12]:
        		return 31
		elif month == 2:
			if isYearLeap(year):
				return 29
			else:		
				return 28
		else:
			return 30

def dayOfYear(year, month, day):
    days = 0
    for m in range(1, month):
        md = daysInMonth(year,m)
        if md == None:
            return None
        days += md
    md = daysInMonth(year, month)
    if md == None or month == None:
        return None
    elif day >= 1 and day <= md:
        return days + day
    else:
        return None
while True:
    try:
        x=int(input("Ingrese un año: "))
        y=int(input("Ingrese el mes: "))3
        z=int(input("Ingrese el día: "))
        print(dayOfYear(x, y, z))

    except ValueError:
        print("No se permite ingresar datos alfanuméricos")
    