print("I like to be a module")
print(__name__)

# module.py

if __name__ == "__main__":
    print("I prefer to be a module")
else:
    print("I like to be a module")

print("---2---")
# module.py

counter = 0

if __name__ == "__main__":
    print("I prefer to be a module")
else:
    print("I like to be a module")

print("---3---")
# module.py

#!/usr/bin/env python3 

""" module.py - an example of Python module """

__counter = 0

def suml(list):
	global __counter
	__counter += 1
	sum = 0
	for el in list:
		sum += el
	return sum

def prodl(list):
	global __counter	
	__counter += 1
	prod = 1
	for el in list:
		prod *= el
	return prod

# It's as if the interpreter inserts this at the top
# of your module when run as the main program.
if __name__ == "__main__":
	print("I prefer to be a module, but I can do some tests for you")
	l = [i+1 for i in range(5)]
	print(suml(l) == 15)
	print(prodl(l) == 120)