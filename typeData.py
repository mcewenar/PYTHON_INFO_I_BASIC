#IMPORTANTE:

def isInt(data):
    if type(data) == int:
        print("es entero")
        return True
    elif type(data) == float:
        print("es float")
        return False 
    elif type(data) == str:
        print("es string")
        return None

    
print(isInt(5))
print(isInt(5.0))
print(isInt("5"))
print(isInt("Hola mundo"))


x=input("Ingrese cualquier dato: ")
print(isInt(x))