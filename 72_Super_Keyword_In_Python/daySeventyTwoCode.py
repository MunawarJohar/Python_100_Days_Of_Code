# class ParentClass:
#     def parent_method(self):
#         print("This is the parent method")
        
# class childClass(ParentClass):
    
#     def parent_method(self):
#         print("Munawar")
#         super.parent_method()
        
#     def child_method(self):
#         print("This is the child method")
#         super().parent_method()
        
        
# obj=childClass()
# obj.child_method()

# use super with constructor
class Programmer:
    def __init__(self,name,id):
        self.name=name
        self.id=id
        
class framework:
    def __init__(self,language,code,framework):
        # super().__init__(name,id)
        self.language=language
        self.code=code
        self.framework=framework
        

munawar=Programmer("Munawar Johar",148)
kamal=framework("Javascript","junior coder","Angular")


print(kamal.language)
print(kamal.code)
print(kamal.framework)
        