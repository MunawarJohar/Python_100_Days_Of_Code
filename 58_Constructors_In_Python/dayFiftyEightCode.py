class Programmer:
    # name="Munawar"
    # occupation="Junior Developer"
    def __init__(self,n,o): 
        print("Hello i am a program")
        self.name=n
        self.occupation=o
    
    def info(self):
        print(f"My name is {self.name} and my occupation is {self.occupation}")
        
        
        
# p=Programmer();
# p.info()
# p=Programmer()
p2=Programmer("Munawar Johar","Python Developer")
p2.info()