print("---1---")

print(1/1)

x = int(input())
y = int(input())
x=x%y 
x=x%y
y=y%x
print(y)

print("---2---")
for i in range(-1,1):
    print("#")

print("---3---")

nums = []
vals = nums
vals.append(1)
print(vals,nums)

print("---4---")

nums = []
vals = nums[:]
vals.append(1)
print(nums,vals)
print("---5---")
lst = [0 for i in range(1,3)]
print(lst)

print("---5---")
for i in range(1):
    print("#")
else:
    print("#")
print("---6---")
var = 1
while var < 10:
    print("#")
    var = var << 1

a=1
b=0
c=a&b
d=a|b
e = a^b
print(c+d+e)
print("---7---")
lst = [1,2,3,4]
print(lst[-3:-2])

print("---8---")
nums = [1,2,3]
vals = nums
del vals[1:2]
print(nums,vals)

print("---9---")
nums = [1,2,3]
vals = nums[-1:-2]
print(nums,vals)

print("---10---")
lst1=[1,2,3]
lst2=[]
for v in lst1:
    lst2.insert(0,v)
print(lst2)
print("---11---")
lst = [i for i in range(-1,2)]
print(lst)
print(len(range(-1,2)))

print("---12---")
t=[[3-i for i in range(3)] for j in range(3)]
s=0
for i in range(3):
    s+= t[i][i]
print(s)

print("---13---")
#lst = [[0,1,2,3] for i in range(2)]
#print(lst[2][0])