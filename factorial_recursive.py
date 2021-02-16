def factorial(num):
    if num == 0:
        return 1
    elif num < 0:
        return None
    return num*factorial(num-1)

x = factorial(int(input("Enter number: ")))
# 5! == 5*(4*(3*(2*(1))))
print(x)


#forma recursiva 2:
def factorialFun(n):
    if n < 0:
        return None
    if n < 2:
        return 1
    return n * factorialFun(n - 1)
x = factorialFun(int(input("Enter number: ")))

print(x)

print("----3----")
#FACTORIAL SIN RECURSIÓN:
def factorialFun(n):
    if n < 0:
        return None
    if n < 2:
        return 1
    
    producto = 1
    for i in range(2, n + 1): #IMPORTANTE
        producto *= i
    return producto
#n = int(input("Enter the number"))
for n in range(1, 6): #probando
    print(n,"--->",factorialFun(n))