#print(None + 1)

#def fun(x):
#    global y
#    y = x*x
#    return y
#fun(2)
#print(y)

def any():
    print(var + 1, end="")
    #print(type(var))
var = 1
any()
print(var)

dct = {"one": "two", "three":"one","two":"three"}
v = dct["one"]
for k in range(len(dct)):
    v = dct[v]
print(v) #pasa el valor, no la clave

tup = (1,2,4,8)
tup = tup[1:-1]
print(tup)
tup = tup[0]
print(tup)

i=0
while i <= 3:
    i +=2
    print("*")
print("Asterisco 2")
i = 0
while i <= 5:
    i += 1
    if i % 2 == 0:
        break
    print("*")

for i in range(1): #Un loop for junto a un else, se ejecutan ambos
    print("#")
else:
    print("#")

print("Hashes 2")

var = 1
while var < 10:
    print("#")
    var = var << 1 #Bitwise operator

z=10
y=0
x=y<z and z > y or y > z and z < y
print(x)


print("Bitwise")
a=1
b=0
c=a & b
d = a | b 
e = a ^ b
print(c + d + e)


lst = [3,1,-2]
print(lst[lst[-1]])

print("corte de lista 2")
lst = [1,2,3,4]
print(lst[-3:-2])

print("Lista 3")
vals = [0,1,2]
vals.insert(0,1)
del vals[1]
print(vals)

print("COpia de listas")

nums = [1,2,3]
vals = nums
del vals[1:2]
print(len(nums))
print(len(vals))

nums = [1,2,3]
vals = nums[-1:-2]
print(len(nums),len(vals))

lst = [1,2,3]
for v in range(len(lst)):
    lst.insert(1,lst[v])
print(lst)


print("Otra de listas")
lst = [1,2,3]
for v in range(len(lst)):
    lst.insert(1,lst[v])
print(lst)

lst = [i for i in range (-1,2)]
print(len(lst))

t = [[3-i for i in range(3)] for j in range(3)]
s = 0
for i in range(3):
    s += t[i][i]
print(s)

print(1//2*3)


x=int(input())
y=int(input())
x=x%y
x=x%y
y=y%x 
print(y)

print("prueba")
z=y=x=1
print(x,y,z,sep="*") #SEPARA CON *
