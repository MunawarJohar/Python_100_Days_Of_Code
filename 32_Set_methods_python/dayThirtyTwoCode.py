# s1={1,2,5,6}
# s2={3,6,7}
# s3=s1.union(s2)
# print(s3)
# #print both set s1 and s2
# print(s1,s2)

# #print s1 before update
# print(s1)
# s1.update(s2)
# print(s1)
# #s1 set is update 

# name1={"Munawar","ali","kamal",148}
# name2={"Ali","Munawar","kamal",1}
# intersection_name=name1.intersection(name2)
# print(intersection_name)

# #before update
# print(name2)
# #after update
# name2.update(name1)
# print(name2)


#Symmetric difference an symmetric difference update
# set1={12,11,23,11,121}
# set2={21,11,12,122,1}
# set3=set1.symmetric_difference(set2)
# print(set3)
# #print before update
# print(set1)
# #print update symmetric difference update
# set1.symmetric_difference_update(set2)
# print(set1)


# city1={"Karachi","Skardu","Kmg","Lahore"}
# city2={"Skd","Karachi","Kmg","Multan"}
# city3=city1.difference(city2)
# print(city3)
# #city2 before update
# print(city2)
# city2.difference_update(city1)
# #after difference update
# print(city2)

# item1={"bag","cake","bat"}
# item2={"dog","cat","red"}
# disjoint=item1.isdisjoint(item2)
# print(disjoint)

# setno1={"bag","cake","bat"}
# setno2={"dog","cat","red","cake","bag","bat"}
# issupperSet=setno1.issuperset(setno2)
# print(issupperSet)

# course={"Java","python","C++"}
# #before adding javaScript
# print(course)
# course.add("JavaScript")
# #affter adding javaScipt
# print(course)


# Set1={2,4,5,6,2,1}
# Set2={3,5,6,7,8,10}
# #before update
# print(Set1)
# Set1.update(Set2)
# #after update
# print(Set1)



# Set5={2,4,5,6,2,1}
# #before remove
# print(Set5)
# Set5.remove(5)
# #after remove
# print(Set5)
# Set5.remove(148)
# print(Set5)

# student={"ALI","Kamal","Zubair","Munawar"}
# std_pop=student.pop()
# print(student)
# print(std_pop)

# del_student={"ALI","Kamal","Zubair","Munawar"}
# del del_student
# print(del_student)

# clear_name={"Ahmed","Munawar","Ameer","Qasim"}
# clear_name.clear()
# print(clear_name)

check_list={"Munawar","Raziq","Kamal","Ali","MaRaj"}
if "Munawar" in check_list:
    print("Munawar Is present in list")
else:
    print("Munawar is not present in list")