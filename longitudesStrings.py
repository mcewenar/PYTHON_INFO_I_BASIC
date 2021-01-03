while True:
    print("It's a program that us allow to know the lenght between two strings /n") 
    def str_more_short(x,y):
        if len(x) < len(y):
            return " {0} is less than {1}".format(x,y)
        elif len(y) < len(x):
            return " {0} is highter than {1}".format(x,y)
        else:
            return "The lenght is equal"


    z = str_more_short((input("#1: ")),(input("#2: ")))
    print(z)