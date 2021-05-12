#class A:
#    def __init__(self,v):
#        self.__a=v+1

#a = A(0)
#print(a.__a)

print("---2---")

class A:
    def __init__(self,v=1):
        self.v=v
    
    def set(self,v):
        self.v=v
        return v

a = A()
print(a.set(a.v + 1))

print("---3---")

class A:
    X = 0
    def __init__(self,v=0):
        self.Y=v
        A.X+=v
a = A()
b=A(1)
c=A(2)
print(c.X)

print("---4---")
class A:
    A=1
print(hasattr(A,"A"))

print("---5---")

#class A:
#    def __init__(self):
#        pass
#a=A(1)
#print(hasattr(a,"A")) GENERA ERROR

print("---6---")
class A:
    def __str__(self):
        return "a"
class B(A):
    def str__(self):
        return "b"
class C(B):
    pass
o=C()
print(o)


print("---7---")
class A:
    pass
class B(A):
    pass
class C(B):
    pass
print(issubclass(C,A))

print("---8---")

class A:
    def a(self):
        print("a")
class B:
    def a(self):
        print("b")
class C(B,A):
    def c(self):
        self.a()
o = C()
o.c()

print("----9----")

class A:
    def __str__(self):
        return "a"
class B(A):
    def __str__(self):
        return "b"
class C(B):
    pass
o = C()
print(o)

print("---10---")

class A:
    V=2
class B(A):
    v=1
class C(B):
    pass
o=C()
print(o.v)

print("---11---")

def f(x):
    try:
        x=x/x
    except:
        print("a",end="")
    else:
        print("b",end="")
    finally:
        print("c",end="")
f(1)
f(0)

print("---12---")

try:
    raise Exception(1,2,3)
except Exception as e:
    print(len(e.args))

print("---13---")

class Ex(Exception):
    def __init__(self,msg):
        Exception.__init__(self,msg+msg)
        self.args = (msg,)
try:
    raise Ex("ex")
except Ex as e:
    print(e)
except Exception as e:
    print(e)

print("---14---")

def I(n):
    s="+"
    for i in range(n):
        s+=s
        yield s
for x in I(2):
    print(x,end="")

print("---15---")
def o(p):
    def q():
        return "*"*p
    return q
r = o(1)
s = o(2)
print(r()+s())


print("---16---")
if (7>5>3):
    print("True")
else:
    print("False") #True, pero en Javascript arroja False, porque se lee de izq. a derecha,
    #pero en Python se lee de derecha a izquierda

print("segunda parte: ", True>3,True>False)