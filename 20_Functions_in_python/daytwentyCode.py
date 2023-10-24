def calcuteGmean(a,b):
    mean=(a*b)/(a+b)
    print(mean)
def isgreater(a,b):
    if(a>b):
        print("First number is greater")
    else:
        print("Second number is greater or equal")

a=9
b=8

# gmean=(a*b)/(a+b)
# print(gmean)
isgreater(a,b)
calcuteGmean(a,b)

c=8
d=7
isgreater(c,d)
# gmean2=(c*d)/(c+d)
# print(gmean)

calcuteGmean(c,d)



def name(fname,lname):
    print("Hello,",fname,lname)
name("Munawar","Hussain")