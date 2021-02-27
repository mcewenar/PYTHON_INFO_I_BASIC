tup = (1, ) + (1, )
tup = tup + tup
print(len(tup))
print("---2---")
def f(x):
    if x==0:
        return 0
    return x + f(x-1)
print(f(3)) 
print("---3---")
def fun(x):
    x += 1
    return x
x = 2
x = fun(x+1)
print(x)

print("---4---")
dct = { }
lst = ["a","b","c","d"]
for i in range(len(lst)-1):
    dct[lst[i]] = (lst[i], )
for i in sorted(dct.keys()):
    k = dct[i]
    print(k[0])

print("---5---")
#def func(a,b):
#    return a**a
#print(func(2)) ERRORRRRRRRR
#def fun(a=b=0): ERRORRRRRRRRRRRRRR
 #   return
def fun(x):
    global y 
    y = x*x
    return y 

fun(2)
print(y) #4

print("---6---")
def any():
    print(var + 1, end="")
var = 1
any()
print(var) #WHY?
print("---7---")
#lista = ["Mary", "had","a","little","lamb"]
#def lista(lst):
#    del lst[3]
#    lst[3] = "ram"
#print(lista(lista)) ERRORRRRR

def fun(x,y,z):
    return x+2*y+3*z
print(fun(0,z=1,y=3))
print("---8---")
dct = {"one":"two","three":"one","two":"three"}
v = dct["one"]
for k in range(len(dct)):
    v = dct[v]
print(v)
print("---9---")
tup = (1,2,4,8)
tup = tup[1:-1]
print(tup)
tup = tup[0]
print(tup)

print("---9---")
#def func1(a):
#    return None
#def func2(a):
#    return func1(a)*func1(a)
#print(func2(2)) ERRORRRRRRRRRRRRRR
#def func(a,b):
#    return b**a
#print(func(b=2,2)) ERROR. SIEMPRE ARGUMENTO POSICIONAL PRIMERO Y 
#LUEGO LOS DE ASIGNACIÓN

list = [x*x for x in range(5)]
def fun(lst):
    del lst[lst[2]]
    return lst
print(fun(list))

print("---10---")
x=1
y=2
x,y,z=x,x,y
z,y,z=x,y,z
print(x,y,z)
print("---11---")
a=1
b=0
a=a^b
print(a)
b=a^b
print(b)
a=a^b
print(a,b) #BITWISE OPERATOR

print("---11---")
nums = [1,2,3]
vals = nums
del vals[:]
print(nums,vals)

print("---12---")
#x=int(input())
#y=int(input())
#x=x%y
#x=x%y
#y=y%x
#print(y)

x=1//5+1/5
print(x)
print(4**(1/2))
print("----13----")
def fun(x,y):
    if x==y:
        return x
    else:
        return fun(x,y-1)
print(fun(0,3))

print("---14---")
#i=0
#while i < i + 2:
#    i += 1
#    print("*")
#else:
#    print("*") BUCLE INFINITO

tup = (1,2,4,8)
tup = tup[-2:-1]
tup = tup[-1]
print(tup)
print("---15---")
dd = {"1":"0","0":"1"}
for x in dd.values():
    print(x,end="")
print("----15----")
dct={}
dct["1"]=(1,2)
dct["2"]=(2,1)

for x in dct.keys():
    print(dct[x][1],end="")

print("----16----")
lst=[[x for x in range(3)] for y in range(3)]
for r in range(3):
    for c in range(3):
        if lst[r][c]%2 !=0:
            print("#")