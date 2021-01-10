#Prioridad	Operador (more)	
#1	+, -	unario
#2	**	
#3	*, /, %	
#4	+, -	binario (less)


print((-2/4), (2/4), (2//4), (-2//4))

keywords = ['False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
#Ex: list,Break, True, and so on
#Son llamadas palabras clave o (mejor dicho) palabras reservadas. 
#Son reservadas porque no se deben utilizar como nombres: ni para variables, ni para funciones, 
#ni para cualquier otra cosa que se desee crear.


for i in keywords:
    print(i)