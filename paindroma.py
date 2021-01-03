a=input("Enter word")
def Convert(string): 
    li = list(string.split("-")) 
    return li 
a1=a.reverse()
if a==a1:
    print("Es palíndroma")
else: 
    print("No es palíndroma")