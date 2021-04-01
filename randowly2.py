print(__name__) #Porque es principal

print("---2---")

try: 
    raise Exception
except BaseException:
    print("a")
except Exception:
    print("b")
except:
    print("c") 

print("---3---")

try:
    raise Exception
except:
    print("c")
#except BaseException:
#    print("a")

#except Exception:
#    print("b")

print("---4---")
x="\\\\"
print(len(x))
#x="\\\"
print(len(x))

print("---5---")

class A:
    def __init__(self,v=2):
        self.v=v
    def set(self,v=1):
        self.v += v
        return self.v
a=A()
b=a
b.set()
print(a.v)
print("---6---")
class A:
    A=1
    def __init__(self):
        self.a=0
print(hasattr(A,"a"))

print("---7---")

class A:
    pass
class B(A):
    pass
class C(B):
    pass
print(issubclass(A,C))

print("---8---")
#class A:
#    def __init__(self):
#        pass
#a = A(1)
#print(hasattr(a,"A"))
try:
    raise Exception(1,2,3)
except Exception as e:
    print(len(e.args))

print("FORMA PRIMITIVA DE ITERAR CON UNA FUNCIÓN USANDO RETURN:")
class I:
    def __init__(self):
        self.s="abc"
        self.i=0
    def __iter__(self):
        return self
    def __next__(self):
        if self.i == len(self.s):
            raise StopIteration
        v = self.s[self.i]
        self.i += 1
        return v
for x in I():
    print(x, end="")

print("---9---")

def o(p):
    def q():
        return "*"*p
    return q
r = o(1)
s=o(2)
print(r()+s())

print("--10--")
#for x in open("file","rt"):
#    print(x)

print("---10---")

str1 = "string"
str2=str1[:]
print(len(str1) == len(str2))

print("---10---")
#str = "abcdef"
#def fun(s):
#    del s[2]
#    return s
#print(fun(str))
x,y,z=3,2,1
z,y,x = x,y,z
print(x,y,z)

print("---11---")
def fun(x):
    return 1 if x%2!=0 else 2
print(fun(fun(1)))

print("---12---")
print(len((1, )))

print("---13---")
d = {1:0,2:1,3:2,0:1}
x=0

for y in range(len(d)):
    x = d[x]
print(x)

print("---14---")
v=1+1//2+1/2+2
print(v)
t=(1, )
t=t[0]+t[0]
print(t)

print("---15---")
d = {"uno":1,"tres":3,"dos":2}
for k in sorted(d.values()): #Organiza el código de menor a mayor
    print(k,end=" ")

print("---16---")
lt = [1,2,3,4]
lt = list(map(lambda x: 2*x,lt))
print(lt)

print("---17---")
i = 4
while i > 0:
    i -= 2
    print("*")
    if i == 2:
        break
else:
    print("*") #No se ejecuta el else si se ejecuta el while

print("----18----")
t=(1,2,3,4)
t=t[-2:-1]
t=t[-1]
print(t)

print("---19---")
d={}
d["2"]=[1,2]
d["1"]=[3,4]
for x in d.keys():
    print(d[x][1],end="")

print("----20----")

def fun(d,k,v):
    d[k]=v
dc = {}
print(fun(dc,"1","v"))