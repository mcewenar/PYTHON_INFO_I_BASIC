#OPERADORES BITWISE (lógica desde adentro) (IMPORTANTE)
#Sin embargo, hay cuatro operadores que le permiten manipular bits de datos individuales.
#Se denominan operadores bitwise.

#Cubren todas las operaciones que mencionamos anteriormente en el contexto lógico, y un operador adicional. 
#Este es el operador xor (como en o exclusivo ), y se denota como ^ (signo de intercalación).

#Aquí están todos ellos:
#1==True
#0==False

# &  (ampersand) - conjunción a nivel de bits.
# |  (barra vertical) - disyunción a nivel de bits.
# ~  (tilde) - negación a nivel de bits.
# ^  (signo de intercalación) - exclusivo a nivel de bits o (xor).


#Arg A 	Arg B 	Arg B & Arg B 	Arg A | Arg B 	Arg A ^ Arg B 
#0	      0	          0	              0	               0
#0	      1	          0	              1	               1
#1	      0	          0	              1	               1
#1	      1	          1	              1	               0


#Operaciones bitwise (~)
#        Arg	~Arg
#        0	      1
#        1	      0


#Hagámoslo más fácil:

# &  requieres exactamente dos  1  s para proporcionar  1  como resultado.
# |  requiere al menos un  1  para proporcionar  1  como resultado.
# ^  requiere exactamente un  1  para proporcionar  1  como resultado.

#Agreguemos un comentario importante: los argumentos de estos operadores deben ser enteros. 
#No debemos usar flotantes aquí.

#La diferencia en el funcionamiento de los operadores lógicos y de bits es importante: 
#los operadores lógicos no penetran en el nivel de bits de su argumento. Solo les interesa el valor entero final.

#Los operadores bitwise son más estrictos: tratan con cada bit por separado. 
#Si asumimos que la variable entera ocupa 64 bits (lo que es común en los sistemas informáticos modernos), 
#puede imaginar la operación a nivel de bits como una evaluación de 64 veces del operador lógico para cada par de bits 
#de los argumentos. Su analogía es obviamente imperfecta, 
#ya que en el mundo real todas estas 64 operaciones se realizan al mismo tiempo (simultáneamente).


#Puede ser un poco sorprendente: el valor de la variable bitneg es -16. 
# Esto puede parecer extraño, pero no lo es en absoluto. Si deseas obtener más información, 
# debes consultar el sistema de números binarios y las reglas que rigen los números de complemento de dos.

#i	0000000000000000000000000000  1111  
#bitneg = ~i 	1111111111111111111111111111  0000  
#Cada uno de estos operadores de dos argumentos se puede utilizar en forma abreviada. 
#Estos son los ejemplos de sus notaciones equivalentes:

#x = x & y 	x &= y 
#x = x | y 	x |= y
#x = x ^ y 	x ^= y

#########################################################


#La variable almacena la información sobre varios aspectos de la operación del sistema. 
#Cada bit de la variable almacena un valor de si/no. También se te ha dicho que solo uno de estos bits es tuyo, 
#el tercero (recuerda que los bits se numeran desde cero y el número de bits cero es el más bajo, mientras que el más alto es el número 31). 
#Los bits restantes no pueden cambiar, porque están destinados a almacenar otros datos. Aquí está tu bit marcado con la letra x:

#flagRegister = 000000000000000000000000000000x000




#Desplazamiento izquierdo binario y desplazamiento derecho binario
#Python ofrece otra operación relacionada con los bits individuales: shifting. Esto se aplica solo a los valores de número entero, 
#y no debe usar flotantes como argumentos para ello.
#Ya aplicas esta operación muy a menudo y muy inconscientemente. ¿Cómo multiplicas cualquier número por diez? Echa un vistazo:

#12345 × 10 = 123450 

#Como puede ver, multiplicar por diez es de hecho un desplazamiento de todos los dígitos a la izquierda y llenar el vacío resultante con cero.

#¿División entre diez? Echa un vistazo:

#12340 ÷ 10 = 1234 

#Dividir entre diez no es más que desplazar los dígitos a la derecha.

#La computadora realiza el mismo tipo de operación, pero con una diferencia: como dos es la base para los números binarios (no 10), 
#desplazar un valor un bit a la izquierda corresponde a multiplicarlo por dos ; 
#respectivamente, desplazar un bit a la derecha es como dividir entre dos (observe que se pierde el bit más a la derecha).

#Los operadores de cambio en Python son un par de dígrafos: < < y > >, sugiriendo claramente en qué dirección actuará el cambio.

#valor << bits
#valor >> bits 

#El argumento izquierdo de estos operadores es un valor entero cuyos bits se desplazan. El argumento correcto determina el tamaño del turno.

#Esto demuestra que esta operación ciertamente no es conmutativa.

#La prioridad de estos operadores es muy alta. Los verás en la tabla de prioridades actualizada, que te mostraremos al final de esta sección.

#Echa un vistazo a los cambios en la ventana del editor.

#La invocación final de print() produce el siguiente resultado:

#17 68 8 

#Nota:

#17 // 2 → 8 (desplazarse hacia la derecha en un bit equivale a la división de enteros en dos)
#17 * 4 → 68 (desplazarse hacia la izquierda dos bits es lo mismo que multiplicar números enteros por cuatro).

#Y aquí está la tabla de prioridades actualizada , que contiene todos los operadores presentados hasta ahora:

#Prioridad	Operador	
#1	           ! ~ (tipo) ++ -- + - 	unario
#2	            **	
#3	            * / % 	
#4	            + - 	binario
#5	            << >> 	
#6	            <<=>> = 	
#7	            == != 	
#8	            &	
#9	            |	
#10	            &&	
#11	            ||	
#12	            = += -= *= /= %= &= ^= |= >>= <<=


var = 17
varRight = var >> 1
varLeft = var << 2
print(var, varLeft, varRight)



#2. Puedes utilizar operadores bit a bit para manipular bits de datos individuales. Los siguientes datos de muestra:

#x = 15, el cual es  0000 1111  en binario.
#y = 16, el cual es  0001 0000  en binario.


x = 4
y = 1

a = x & y
b = x | y
c = ~ x
d = x ^ 5
e = x >> 2
f = x << 2

print(a, b, c, d, e, f) 
