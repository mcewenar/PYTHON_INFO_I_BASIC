ls = [[c for c in range(r)] for r in range(3)]
for x in ls:
    if len(x) < 2:
        print("a")

print("---2---")

try:
    raise Exception
except BaseException:
    print("a",end='')
else:
    print("b,",end="")
finally:
    print("c")

print("---3---")
class A:
    def __init__(self,name):
        self.name=name
a = A("class")
print(a)

print("---4---")
try:
    raise Exception
except:
    print("c")
#except BaseException:
    #print("a")
#except Exception:
    #print("b")
print("---5---")

class X:
    pass
class Y(X):
    pass
class Z(Y):
    pass
x=X()
z=Z()
print(isinstance(x,Z),isinstance(z,X)) #FALSE TRUE

print("----6----")
x="""
"""
print(len(x))

print("---7---")
#class Class:
#    def __init__(self):
#        pass

#c=Class(None)

class A:
    A=1
    def __init__(self,v=2):
        self.v = v+A.A
        A.A+=1
    def set(self,v):
        self.v += v
        A.A+=1
        return
a=A()
a.set(2)
print(a.v)

print("----8----")
class A:
    A=1
    def __init__(self):
        self.a=0
print(hasattr(A,"A"))

print("----9----")
class A:
    pass
class B:
    pass
class C(A,B):
    pass
print(issubclass(C,A) and issubclass(C,B))

print("---10---")

#class A:
#    def __init___(self,v):
#        self._a=v+1
#a=A(0)
#print(a._a)

print("---11---")
#class A:
#    def __init__(self):
#        pass
#    def f(self):
#        return 1
#    def g():
#        return self.f()
#a = A()
#print(a.g())

print("---12---")
def I(n):
    s = ''
    for i in range(n):
        s+='*'
        yield s 
for x in I(3):
    print(x,end='')

print("---13---")
def a(x):
    def b():
        return x+x
    return b
x = a("x")
y=a("")
print(x() + y())


print("---13---")

a=2_2_2
b=2
print(a*b)