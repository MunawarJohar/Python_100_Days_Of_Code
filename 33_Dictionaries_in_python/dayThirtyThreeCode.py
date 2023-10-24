# dictionary={148:"Munawar",150:"Syed hussain ",149:"Zulfiqar Ali",1:"Akbar"}
# print(dictionary)
# print(dictionary[148])

information={1:"Sajid",2:"Kamal",3:"Qadir",4:"Munawar",5:"Abid"}
print(information[1])
#accessing using get method
# print(information.get(4))
# print(information.get(3))
#key method
# print(information.keys())
# for key in information.keys():
#     print(f"The corresponding values of the {key} is {information[key]}")

#accessing multiple values
# print(information.values())

#key value pairs
new_info={1:"Kamal",2:"Munawar",3:"Jawahir",4:"Sohail"}
print(new_info.items())
for key,value in new_info.items():
    print(f"The corresponding values of the {key} is {new_info[key]}")


