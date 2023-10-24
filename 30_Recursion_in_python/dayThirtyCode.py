#Factorial (5)
#5*4*3*2*1 =120
#factorial (0)=1
# factorail(n)=n*factorail(n-1)


def Factorail(n):
    if (n==1 or n==0):
        return 1
    else:
        return n*Factorail(n-1)
    
print(Factorail(5))