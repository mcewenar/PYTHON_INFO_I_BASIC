
def repi(base):
    if base=="T":
        return "A"
    elif base=="A":
        return "T"
    elif base=="C":
        return "G"
    elif base=="G":
        return "C"
    else:
        return " "
    
def trans(adncomp):
    if adncomp=="T":
        return "A"
    elif adncomp=="A":
        return "U"
    elif adncomp=="C":
        return "G"
    elif adncomp=="G":
        return "C"
    else:
        return " "
def tra(adntrans):
    for amino in range(0,1000,3):
    
        if adntrans=="AUG":
            return "M"
        if adntrans=="UUU" or adntrans=="UUC":
            return "F"
        elif "UUA"==adntrans or "UUG"==adntrans or "CUU"==adntrans or  "CUC"==adntrans or "CUA"==adntrans or "CUG"==adntrans:
            return "L"
        elif "AUU"==adntrans or "AUC"==adntrans or "AUA"==adntrans:
            return "I"
        elif "GUU"==adntrans or "GUC"==adntrans or  "GUA"==adntrans or "GUC"==adntrans:
            return "V"
        elif "UCU"==adntrans or "UCC"==adntrans or "UCA"==adntrans or "UCG"==adntrans:
            return "S"
        elif "CCU"==adntrans or "CCC"==adntrans or "CCA"==adntrans or "CCG"==adntrans:
            return "P"
        elif "ACU"==adntrans or "ACC"==adntrans or "ACA"==adntrans or "ACG"==adntrans:
            return "T"
        elif "GCU"==adntrans or "GCC"==adntrans or "GCA"==adntrans or "GCG"==adntrans:
            return "A"
        elif "UAU"==adntrans or "UAC"==adntrans:
            return "Y"
    ##  elif UAA==adntrans or UAG==adntrans or UGA==adntrans:
    ##            
        elif "CAU"==adntrans or "CAC"==adntrans:
            return "H"
        elif "CAA"==adntrans or "CAG"==adntrans:
            return "Q"
        elif "AAU"==adntrans or "AAC"==adntrans:
            return "N"
        elif "AAA"==adntrans or "AAG"==adntrans:
            return "K"
        elif "GAU"==adntrans or "GAC"==adntrans:
            return "D"
        elif "GAA"==adntrans or "GAG"==adntrans:
            return "E"
        elif "UGU"==adntrans or "UGC"==adntrans:
            return "C"
        elif "UGG"==adntrans:
            return "W"
        elif "CGU"==adntrans or "AGA"==adntrans or "AGG"==adntrans or "CGC"==adntrans or "CGA"==adntrans or "CGG"==adntrans:
            return "R"
        elif "AGU"==adntrans or "AGC"==adntrans:
            return "S"
        elif "GGU"==adntrans or "GGC"==adntrans or "GGA"==adntrans or "GGG"==adntrans:
            return "G"
        else:
            return " "
        
            
            
        
            
        
while True:
    
    
    adn=input("escriba la secuencia de ADN EN MAYÚSCULAS")
    adncomp=""
    for GCTA in adn:
        print(GCTA + " el complementario es: " + repi(GCTA))
        adncomp=adncomp+repi(GCTA)
    print(adn)
    print(adncomp)



    adntrans=""
    for GCTA in adncomp:
        print(GCTA + " el transcrito es " + trans(adncomp))
        adntrans=adncomp+trans(GCTA)
    print(adn)
    print(adncomp)
    print(adntrans)
    print("-------")


    print("el aminoácido es:"+ tra(adntrans))
        
    print("------------")
    x=int(input("si desea ingresar otra secuencia de nucleótidos, por favor ingrese 1; escriba 2 para salir"))
    if x==1:
        continue
    elif x==2:
        print("feliz día")
        break
    

    
