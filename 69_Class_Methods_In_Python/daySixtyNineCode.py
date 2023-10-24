class Programmer:
    company="Google"
    def show(self):
        print(f"the name of programmer is {self.name} and company name is {self.company}")

    @classmethod
    def ChangeCompny(cls,newCompany):
        cls.company=newCompany
        
        
p1=Programmer();
p1.name="Munawar"
p1.show()        

p1.ChangeCompny("Apple")
p1.show()
print(p1.company)