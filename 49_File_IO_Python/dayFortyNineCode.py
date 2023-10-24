# f=open('myfile2.txt','w')
# f.write("File IO")
# f.close()
# print(f)
# text=f.read()
# print(text)
# f.close()
# file=open('myfile.txt','r')
# content=file.read()
# print(content)

with open('myfile.txt','a') as newFile:
    newFile.write("This is new content")