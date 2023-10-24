class Person:
    name="Munawar"
    occupation="Programmer"
    salary=40000
    
    def information(self):
        print(f"{self.name} is a {self.occupation}")
    
p=Person()

p.name="Munawar Johar"
p.salary=50000
#print(p.name,p.occupation)
p.information()


b=Person()
b.name="Kamal"
b.occupation="Developer"

b.information()

c=Person()
c.information()