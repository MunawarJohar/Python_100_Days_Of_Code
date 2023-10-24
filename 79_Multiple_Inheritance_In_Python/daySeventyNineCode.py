class Programmer:
    def __init__(self,name):
        self.name=name
    def show(self):
        print(f"The name is {self.name} ")

class Singer:
    def __init__(self,singer):
        self.singer=singer
        
    def show(self):
         print(f"The name is {self.singer} ")
    

class SingerProgrammer(Programmer,Singer):
    def __init__(self,singer,name):
        self.singer=singer
        self.name=name
        
        
pro=SingerProgrammer("Kardiya Dill Tere Nuam","Munawar")
print(pro.name)
print(pro.singer)
pro.show()
print(SingerProgrammer.mro())
# mro stand method resolution order