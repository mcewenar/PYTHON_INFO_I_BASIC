##print("Promedio de 5 notas")
##a=float (input("Ingrese la primera nota"))
##b=float (input("ingrese la segunda nota"))
##c=float (input("ingrese la tercera nota"))
##d=float (input("ingrese la cuarta nota"))
##e=float (input("ingrese la quinta nota"))
##a=a*0.30
##print(a)
##b=b*0.15
##print(b) 
##c=c*0.15
##print(c)
##d=d*0.20
##print(d)
##e=e*0.20
##print(e)
##
##p=(a+b+c+d+e)
##print(p)
##if p>=3.0:
##    print("aprobÃ³ el curso")
##elif p<3.0:
##    print("te metieron la verga")

##
##i=1
##while i<=5:
##   print(i)
##   i=i+1


##for i in range(5):
## print("hola MUNDO")
## print(i)

##hce=[]
##paciente=[]
##for i in range(0,1000,1):
##   a=input("Ingrese el nombre del paciente")
##   b=int(input("ingrese identificaciÃ³n"))
##   c=int(input("ingrese la edad"))
##   d=input("ingrese la EPS")
##   pacientes=[a,b,c,d]
##   hce.append(pacientes)
##   resultado=(int(input("Â¿Desea ingresar otro usuario? SÃ­=1 o No=2")))
##   if resultado==1:
##      continue
##
##   else:
##      break
##input("ACTIVIDAD 3, CALCULADORA")
##a=input("escoger una operacion aritmÃ©tica elemental: suma=1, resta=2, multiplicaciÃ³n=3, 4=divisiÃ³n, 5=salir")
##if(a==1):
##   x=int(input("elija UN nÃºmeros a sumar"))
##   y=int(input("elija otro nÃºmero a sumar"))
##   a=input(x+y)
##elif a==2:
##   x=int(input("elija un nÃºmero a restar"))
##   y=int(input("elija otro nÃºmero a restar"))
##   a=input(x-y)
##   
## else:


##def mi_func():
##   print("hola")
##   print("bioingenieros")
##   print("udea")
##mi_func()
##
##
##z=mi_func(x)
##print(z)
##



##def maximo(x,y):
##   if x>y:
##      print("el numero mayor es")
##      return x
##   elif y>x:
##      print("ek nÃºmero mayor es:")
##      return y
##   else:
##      print("los nÃºmeros ingresados son iguales")
##      return x,y
##print(maximo(4,7))   
##


##import math
##from math import pi
##from math import cos
##print(math.pi)
##a=int(input("ingrese un Ã¡ngulo"))
##print(math.cos(a))


##Algoritmo para triángulos:
    ##import math
##from math import pi
##from math import cos
##print(math.pi)
##a=int(input("ingrese un ángulo"))
##print(math.cos(a))


##from fsuma import fibo
##from fsuma import suma as opsum
##
##x=int(input("ingrese #1: "))
##y=int(input("ingrese #2: "))
##print(opsum(x,y))
##print("-----------------------")
##f=int(input("halle el número de fibonacci menor al que ingrese: "))
##fibo(f)
##
##tri=int(input("si desea calcular ángulo lado ángulo escriba 1, ó 2 si desea saber lado ángulo lado a l"))
##if tri==1:
##    an1=int(input("por favor ingrese el ángulo a"))
##    la1=int(input("ingrese lado a"))
##    an2=int(input("ingrese angulo b"))
##    an3=int(input(180-(an1+an2)))
##    print(an1)
##            
##            
##elif tri==2:
##    la1=int(input("ingrese el lado 1"))
##    an1=int(input("ingrese el ángulo 1"))
##    la2=int(input("ingrese el lado 2"))
##    la3=math.sqrt(la1**2+la2**2-2*la1*la2*math.cos(math.radians(an1)))
##    print(la3)
##    an2=math.asin(la1*math.sin(an1)/la3)
##    print(an2)
##    an3=180-(an1
##    
##    
##def impura(arg):
##    lista.append(arg)
##    return lista
##lista=[]
##print(impura(("bio",3)))
##print(impura(2018))


##b=(lambda x,y:print(x+y))
##c=b(4,3)

##def factorial(x):
##    if x==0:
##        return 7
##    else:
##        return (factorial(x-1)+2)
##print(factorial(4))

##while True:
##    try:
##        num1=int(input("Ingrese el numerador:"))
##        num2=int(input("ingrese el denominador:"))
##        print(num1/num2)
##        print("división correcta")
##        break
##    except ZeroDivisionError:
##        print("error tipo #/0")
##    except ValueError:
##        print("Datos no compatible")


##print("Calculadora sencilla")
##a=int(input("escoger una operacion aritmética elemental: suma=1, resta=2, multiplicaciÃ³n=3, 4=divisiÃ³n, 5=salir"))
##while True:
##     try:
##        if a==1:
##            x=int(input("elija un número a sumar"))
##            y=int(input("elija otro número a sumar"))
##            print(x+y)
##            break
##        elif a==2:
##            x=int(input("elija un número a restar"))
##            y=int(input("elija otro número a restar"))
##            print(x-y)
##            break
##        elif a==3:
##            x=int(input("elija un número a multiplicar"))
##            y=int(input("elija otro número a multiplicar"))
##            print(x*y)
##            break
##        elif a==4:
##            x=int(input("elija el numerador"))
##            y=int(input("elija el denominador"))
##            print(x/y)
##            break
##        elif a==5:
##            print("gracias por utilizar la calculadora")
##            break
##     except ValueError:
##            print("¡Error! Sumaste datos incompatibles, vuelve a ingresar los números:")
##     except ZeroDivisionError:
##            print("¡ERROR!Dividiste entre 0, vuelve a ingresar los números")
##
##
##
##


##def funcion(x,y):
##    print(x+y)
##x=int(input("ingrese el #1"))
##y=int(input("ingrese el #2"))
##funcion(x,y)


##def funcion(x,y):
##    if x>y:
##        print("el número mayor es:")
##        return x
##    elif y>x:
##        print("elnumero mayor es:")
##        return y
##    else:
##        print("los números ingresados son iguales")
##        return x,y
##print(funcion(4,7))



##print("calculadora sencilla")
##while True:
##    op=int(input("1=suma, 2=resta, 3=multiplicación, 4=divisón, 5=salir"))
##    if op==1:
##        x=int(input("ingrese el primer"))
##        y=int(input("ingrese el segundo"))
##        def suma(x,y):
##            suma=(x+y)
##            return suma
##        
##        print(suma(x,y))
##        
##    elif op==2:
##        x=int(input("ingrese el primer"))
##        y=int(input("ingrese el segundo"))
##        def resta(x,y):
##            resta=(x-y)
##            return resta
##        print (resta(x,y))
##    elif op==3:
##        x=int(input("ingrese el primer"))
##        y=int(input("ingrese el segundo"))
##        def mult(x,y):
##            mult=(x*y)
##            return mult
##        print(mult(x,y))
##    elif op==4:
##        x=float(input("ingrese el primer"))
##        y=float(input("ingrese el segundo"))
##        if y==0:
##            print("error, división por 0")
##            y=float(input("ingrese el segundo"))
##        else:
##            def div(x,y):
##                div=(x/y)
##                return div
##            print(div(x,y))
##    elif op==5:
##        break
##    else:
##        print("núm incorrecto")
##        
            
        
##print("Historia clinica")
####if op==1:
##def datos():
##    hce=[]
##    for i in range(2):
##            nom=str(input("Nombre y apellido"))
##            eps=str(input("EPS"))
##            ide=int(input("ingrese identificaciÃ³n"))
##            eda=int(input("ingresa edad"))
##            a=(nom,eps,ide,eda)
##            hce.append(a)
##            print(type(hce))
##            print(hce)
##datos()
##op=int(input("1 para continuar"))
##if op==1:
##    def datos():
##        hce=[]
##        for i in range(2):
##                nom=str(input("Nombre y apellido"))
##                eps=str(input("EPS"))
##                ide=int(input("ingrese identificaciÃ³n"))
##                eda=int(input("ingresa edad"))
##                a=(nom,eps,ide,eda)
##                hce.append(a)
##                print(type(hce))
##                print(hce)
##    
##else:
##        break
##    

##print("Historia clinica")
####if op==1:
##while True:
##    try:
##        def datos():
##            hce=[]
##            for i in range(1):
##                    nom=str(input("Nombre y apellido"))
##                    eps=str(input("EPS"))
##                    ide=int(input("ingrese identificaciÃ³n"))
##                    eda=int(input("ingresa edad"))
##                    a=(nom,eps,ide,eda)
##                    hce.append(a)
##                    print(type(hce))
##                    print(hce)
##        datos()
##        op=int(input("1 para continuar, 2 para salir"))
##        if op==1:
##            def datos():
##                hce=[]
##                for i in range(2):
##                        nom=str(input("Nombre y apellido"))
##                        eps=str(input("EPS"))
##                        ide=int(input("ingrese identificaciÃ³n"))
##                        eda=int(input("ingresa edad"))
##                        a=(nom,eps,ide,eda)
##                        hce.append(a)
##                        print(type(hce))
##                        print(hce)
##        
##        elif op==2:
##            break
##        
##    except ValueError:
##        print("Repita el dato")
##        
##    except TypeError:
##        print("una funcion es llamada")
##    except SyntaxError:
##        print("el codigono puede ser analizado")
##    except NameError:
##        print("una variable desconocida")
##    except IndexError:
##        print("falla de importacion")
##    except ImportError:
##        print("error de importacion")



