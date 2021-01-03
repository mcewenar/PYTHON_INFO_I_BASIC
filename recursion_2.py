"""La recursión es un concepto muy importante en la
programación funcional.
También llamadas autorreferencia, son funciones que se
llaman a sí mismas.

Se utilizan para resolver problemas que pueden ser
divididos en subproblemas más sencillos del mismo tipo."""


#Exercise: Rercursión
def factorial(x):
    if x==1:
        return 1
    else:
        return x*factorial(x-1)
x=int(input("enter the number that you Need to generate a factorial: "))
print(factorial(x))