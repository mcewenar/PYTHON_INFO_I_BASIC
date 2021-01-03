var = "Hola mundo!"
print(var[6])



nums = [10,9,8,7,6,5]
nums [0] = nums[1] - 5
if 4 in nums:
    print(nums[3])
else:
    print(nums[4])


nums = [9,8,7,6,5]
nums.append(4)
nums.insert(2,11)
print(len(nums))




letras = ['p','q','r','s','p','u']
numeros = [2,5,8,9,4,5,1,0,5]
print(max(numeros))
print(max(letras))
print(min(numeros))
print(min(letras))
print(numeros.count(5))
print(letras.count('p'))
print(numeros.remove(5))
#print(numeros.remove(3))
print(numeros)
print(letras.remove('r'))
print(letras)
print(numeros.reverse())
print(numeros)
print(letras.reverse())
print(letras)


nums = list(range(3,15,3))
print (nums[2])



palabras = ["Hola","Bioingenieros", "de la", "UdeA"]
cont = 0
max_index = len(palabras) - 1
while cont <= max_index:
    palabra = palabras[cont]
    print (palabra + "!")
    cont += 1