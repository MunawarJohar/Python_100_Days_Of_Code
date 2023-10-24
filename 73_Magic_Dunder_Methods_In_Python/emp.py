class Employee:
    def __init__(self,name):
      self.name=name
    def __len__(self):
        i=0
        for c in self.name:
            i=i+1
        return i
    def __str___(self):
        return f"The name of employee is {self.name} str" 
    def __repr___(self):
        return f"The name of employee is {self.name} repr"