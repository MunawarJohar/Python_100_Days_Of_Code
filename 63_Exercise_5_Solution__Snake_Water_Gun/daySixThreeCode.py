import random
# print(random.randint(0,2))

def check(computer,user):
    if computer==user:
        return 0
    
    if(computer==0 and user==1):
        return -1
    if(computer==1 and user==2):
        return -1
    if(computer==2 and user==0):
        return -1
    return 1

computer=random.randint(0,2)
user=input(("0 for Snake, 1 for water and 2 for Gun: \n"))

score=check(computer,user)
print("You:",user)
print("Computer:",computer)
if(score==0):
    print("Its a draw")
elif(score==-1):
    print("You lose")
    
else:
    print("You Win")
