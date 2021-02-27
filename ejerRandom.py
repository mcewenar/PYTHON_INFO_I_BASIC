lst = [1,2]
for v in range(2):
    lst.insert(-1,lst[v])
print(lst)

print("----2----")
nums = [1,2,3]
vals = nums
print(vals,nums)

print(1//2)

#def func(a,b):
#    return b**a
#print(func(b=2,2)) ERRORRR

list = [x*x for x in range(5)]
def fun(lst):
    del lst[lst[2]]
    return lst
print(fun(list))

print("----3----")
a=1
b=0
a=a^b 
b = a^b 
a = a^b 
print(a,b)

print("----4----")
nums = [1,2,3]
vals = nums
del vals[:]
print(vals)
print(nums)

print(1%2)

print("---5---")
print("a","b","c",sep="sep")


print("----6----")
tupl = 1,2,3
#tupl[1] = tupl[1] + tupl[0] ES INMUTABLE

print("---7---")
x = float(input())
y = float(input())
print(y**(1/x))

print("---8---")
dct = {"uno":"dos","tres":"uno","dos":"tres"}
v = dct["tres"]

for k in range(len(dct)):
    v = dct[v]
print(v)
lst = [i for i in range(-1,-2)]
len(lst)

print("---9---")
def fun(x,y):
    if x == y:
        return x
    else:
        return fun(x, y-1)
print(fun(0,3))

print("----10----")
tup = (1,2,4,8)
tup = tup[-2:-1]
print(tup)
tup = tup[-1]
print(tup)

print("---11---")
dct = {}
dct['1']=(1,2)
dct["2"]=(2,1)

for x in dct.keys():
    print(dct[x][1],end="")

print("---12---")

lst = [[x for x in range(3)] for y in range(3)]

for r in range(3):
    for c in range(3):
        if lst[r][c]%2 != 0:
            print("#")