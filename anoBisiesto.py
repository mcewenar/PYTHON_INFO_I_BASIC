def isYearLeap(year):
    if testData[i]%4!=0:
      return False
    elif testData[i]%100!=0:
        return True
    elif testData[i]%400!=0:
        return False
    else: 
        return True
    
    #FORMA COMPACTA
    #if testData[i] % 4 == 0 and (testData[i] % 100 != 0 or testData[i] % 400 == 0):
	#    return True
    #else:
	#    return False
    

testData = [1900, 2000, 2016, 1987]
testResults = [False, True, True, False]
for i in range(len(testData)):
	yr = testData[i]
	print(yr,"->",end="")
	result = isYearLeap(yr)
	if result == testResults[i]:
		print("OK")
	else:
		print("Error")


while True:
    año = int(input("Introduzca un año: "))

    if año>=1582:
        if año%4!=0:
            print("Año común")
        elif año%100!=0:
            print("Años bisiesto")
        elif año%400!=0:
            print("Año común")
        else: 
            print("Año bisiesto")
    else:
        print("No dentro del período del calendario gregoriano")