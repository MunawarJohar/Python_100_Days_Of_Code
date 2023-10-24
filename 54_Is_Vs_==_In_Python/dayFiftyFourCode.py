a=4
b="4"
# both are operators 
print(a is b) # exact location of object in memory
print(a==b)  # value 


c=[1,2,3]
d=[1,2,3]


print(c is d) #false 
print(c==d) #True 


t1=(1,2,3)
t2=(1,2,3)


print(t1 is t2)
print(t1==t2)


n1=None
n2=None
print(n1 is n2)
print(n1 is None)
print(n1==n2)

m1="Munawar"
m2="Munawar"
print(m1 is m2)
print(m1==m2)

int1=5
int2=5
print(int1 is int2)
print(int1==int2)