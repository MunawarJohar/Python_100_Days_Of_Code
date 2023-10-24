class Vector:
    def __init__(self,i,j,k):
        self.i=i
        self.j=j
        self.k=k
        
    def __str__(self):
        return f"{self.i}i+{self.j}j+{self.k}k"
    
    def __add__(self,x):
        return f"{self.i+x.i}, {self.j+x.j} ,{self.k+x.k}"
    
v1=Vector(2,4,9)
print(v1)

    
v2=Vector(10,20,30)
print(v2)

print(v1+v2)
print(type(v1+v2))