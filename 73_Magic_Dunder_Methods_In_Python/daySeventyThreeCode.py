class programmer:
    name="Munawar"
    
    def __len__(self):
        i=0
        for c in self.name:
            i=i+1
        return i
    
p=programmer()
print(p.name)
print(len(p))