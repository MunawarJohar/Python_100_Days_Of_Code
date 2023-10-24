class Programmer:
    companyName="Google"
    noofProgrammer=0
    def __init__(self,name):
    # name and amount is instance variable
        self.name=name
        self.amount=0.02
        Programmer.noofProgrammer+=1
        
    def ShowDetails(self):
        print(f"The name of Programmer is {self.name} and the amount is {self.amount} and Company Name is {self.companyName} Number of Programmers are {self.noofProgrammer}")
        

p=Programmer("Munawar")
p.ShowDetails()
# Programmer.ShowDetails(p)


p1=Programmer("Kamal")
p1.companyName="Apple"
p1.amount=5.0
p1.ShowDetails()

print(Programmer.companyName)
print(p1.companyName)


# class Myclass:
#     class_variable=0
#     def __init__(self):
#         Myclass.class_variable+=1
        
#     def printClass(self):
#         print(Myclass.class_variable)
        
        
# obj=Myclass()
# obj2=Myclass()
# obj.printClass()
# obj2.printClass()