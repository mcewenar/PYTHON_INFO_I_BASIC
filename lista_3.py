nums = [-1, 2, -3, 4, -5] #MÁS FUNCIONES DE LISTAS
if all([abs(i) < 3 for i in nums]):
    print(1)
else:
    print(2)


nums = [-1, 2, -3, 4, -5]
if any([abs(i) < 3 for i in nums]):
    print(1)
else:
    print(2)