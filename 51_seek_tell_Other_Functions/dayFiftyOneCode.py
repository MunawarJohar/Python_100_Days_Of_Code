# with open('myfile.txt', 'r') as file:
#     print(type(file)) 
#     file.seek(15)
#     print(file.tell())
#     data=file.read(5)
#     print(data)
    
    
with open('myfile.txt','w') as f:
    f.write("Hello World")
    f.truncate(2)
    

with open('myfile.txt','r') as f:
    print(f.read())