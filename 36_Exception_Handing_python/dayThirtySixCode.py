# a =int(input("Enter the number:"))
# print(f"Multipalication table of {a} is :")
# try:
#       for i in range(1,11):
#           print(f"{{int(a) X {i} {i}={int(a)*i}}}")
# except:
#     print("Invalid Error Occur")
     
# print("Some important line of Code")
# print("End of program")


# ValueError
try:
    num=int(input("Enter the number"))
    a=[6,3]
    print(a[num])
except ValueError:
    print("please Number enter an integer")
except IndexError:
    print("Index error")
