# f=open('myfile.txt','r')
# while True:
#     line=f.readline()
#     if not line:
#         break
#     print(line)

# # Read marks from text file

# file=open('marks.txt','r')
# i=0
# while True:
#      i=i+1
#      lines=file.readline()
#      if not lines:
#          break
#      mark1=int(lines.split(",")[0])
#      mark2=int(lines.split(",")[1])
#      mark3=int(lines.split(",")[2])
     
     
#      print(f"The marks of Student {i} in Math is :{mark1*2}")
#      print(f"The marks of Student {i} in Computer Science is :{mark2*2}")
#      print(f"The marks of Student {i} in English is :{mark3*2}")
     
#      print(lines)


# # Writing a content in a file.

# w_file=open('write.txt','w')
# l=['Line\n','line 2 \n','line 3 \n']

# w_file.writelines(l)
# w_file.close()

## add new line 
files=open('write.txt','w')
lin=['line 1','line 2','line 3']
for l in lin:
    files.write(l+"\n")
files.close()