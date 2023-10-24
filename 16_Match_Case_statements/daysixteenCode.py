x=int(input("Enter the value of x :"))
match x:
    case 0:
        print("The value of x is Zero")
    case 1:
        print("The value of x is 1")
    case 4:
        print("The value of x is 4")
    case _ if x!=90:
        print(x,"not 90")
    case _ if x!=80:
        print(x,"is not 30")
    case _:    #this is default statement 
        print(x)   