class programmer:
    def __init__(self,name,salary):
                self.name=name
                self.salary=salary
                
    @classmethod
    def fromString(cls,string):
        return cls(string.split("-")[0],string.split("-")[1])
                
p=programmer("Munawar",148)
print(p.name)
print(p.salary)

string="Munawar-2000"
p1=programmer.fromString(string)
print(p1.name)
print(p1.salary)
