marks=[20,23,24,26,30,55,3,21]
# index=0
# for mark in marks:
#     print(mark)
#     if(index==3):
#         print("Munawar Awasome !") 
#     index=index+1


# for index, mark in enumerate(marks):
#     print(mark)
#     if(index==4):
#         print("Munawar Awasome !") 
#     index=index+1

for index, mark in enumerate(marks,start=2):
    print(mark)
    if(index==4):
        print("Munawar Awasome !") 
    index=index+1