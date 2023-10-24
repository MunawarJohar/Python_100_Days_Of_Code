class Programmer:
    def __init__(self,name,id):
        self.name=name
        self.id=id
        
    def showDetails(self):
        print(f"The name of Programmer is {self.name} and id is : {self.id}")



class JuniorDeveloper(Programmer):
    def showFrameWork(self):
        print("The default frame work is django.")
pro=Programmer("MunawarJohar",148)
pro.showDetails()
pro2=Programmer("Raziq",432)
pro2.showDetails()

jdeveloper=JuniorDeveloper("Kamal Ali",321)
jdeveloper.showDetails()
jdeveloper.showFrameWork()