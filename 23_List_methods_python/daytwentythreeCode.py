l=[12,33,44,56,6]
print(l)
l.append(4)
print(l)

#sort method in python
l.sort()
#sort in ascending order
print(l)

l2=[1,2,3,4,5,6]
print(l2)
l2.reverse()
print(l2)

l3=["hello","Munawar","Hussain","kamal","Munawar","Munawar"]
print(l3)
print(l3.count("Munawar"))


cp=l2.copy()
cp[0]=0
print(cp)

l4=["Munawar",1,"Hussain",1122]
print(l4)
l4.insert(1,148)
print(l4)
l4.insert(1,"Johar")
print(l4)

l5=[1,2,3,4,5]
print(l5)
l6=[6,7,8,9,10]
l5.extend(l6)
print(l5)

a=["Munawar","Raziq","Sharif"]
print(a)
b=[148,1,3]
print(b)
new=a+b
print(new)