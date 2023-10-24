# class Student:
#     def __init__(self):
#         self.name="Munawar"
#         self.__PrivateName="Johar" #this is a private variable 
        
        
        
class Programmer:
    def __init__(self):
        self.Pname="Munawar"
    def _Method(): # protected
        return "MunawarJohar"
    
    
class Developer(Programmer):#inherited 
    pass
    
# s=Student()
# print(s.name)
# # print(s.__PrivateName) #it is cannot be accessiable because it is a private vaiable

# #Can be access indirectly 
# # print(s.__Student__PrivateName)


# # print(s.__dir__)


obj=Programmer();
obj2=Developer()
print(obj.Pname)
print(obj._Method())
# print(obj2._Method())