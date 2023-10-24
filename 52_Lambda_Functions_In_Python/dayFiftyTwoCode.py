# def double(x):
#     return x*2

# print(double(5))

double=lambda x:x*2

cube=lambda y:y*y*y


average=lambda x,y,z:(x+y+z)/3


def appl(fx,value):
    return 6+fx(value)


print("The doube x is :",double(10))

print(f"The cube of 5 is :{cube(5)}")

print("The average is :",average(15,5,20))

print(appl(lambda x:x*x,2))