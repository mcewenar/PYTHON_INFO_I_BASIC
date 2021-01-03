#1.
tupla = (11,22,33,44,55)
res = tuple(filter(lambda x : x%2==0,tupla))
print (res)

#2.
nums = [1,2,5,8,3,0,7]
res = list(filter(lambda x : x < 5, nums))
print(res)