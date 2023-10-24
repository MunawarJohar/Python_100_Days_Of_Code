# l=[2,3,5]
# list2=["Red","Green","Blue","White"]
# print(l)
# print(list2)
# print(type(l))

# marks=["Pass",40,"False",50]
# print(marks[0])
# print(marks[1])
# print(marks[2])
# print(marks[3])


colors=["Red","Green","Blue","Yellow"]
print(colors[0])
print(colors[1])
print(colors[2])
print(colors[3])

#negative index
print(colors[-1])
print(colors[-2])
print(colors[-3])
print(colors[-4])
print(len(colors)-2)

# names=["kamal","Munawar","Ali","Harry"]
# if "Munawar" in names:
#     print("Yes ")
# else:
#     print("No")

# if "Mun" in "Munawar":
#     print("Match")
# print(colors[0:4])
# print(colors[0:4:2])
# print(colors[1:4])
# numbers=[2,4,True,8,10,False,12,14]
# print(numbers[1:-1])
# print(numbers[1:8:3])
# #both below statement are true and python interpreter set correct order
# print(numbers[1:])
# print(numbers[:8])
lists=[i for i in range(10)]
print(lists)
#for condition print event number in list
lists=[i for i in range(10)if i%2==0]
print(lists)