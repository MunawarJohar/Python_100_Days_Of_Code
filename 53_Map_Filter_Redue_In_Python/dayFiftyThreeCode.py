# def cube(x):
#     return x*x*x

# print(cube(5))

l=[1,2,3,4,5,6,10,30]
# # newl=[]
# # for item in l:
# #     newl.append(cube(item))
    
# newl=list(map(cube,l))
# print(newl)


# l2=[1,2,3,4,5,6,10,30,50,100]
# def filter_function(a):
#     return a>5

# newfilter=list(filter(filter_function,l2))
# print(newfilter)

# number=[4,5,7,8,22,44,7]
# evens=filter(lambda x:x%2==0,number)
# print(list(evens))

from functools import reduce

numbers=[1,2,44,3,1,3]

def sum(x,y):
    return x+y

mysum=reduce(sum,numbers)

print(mysum)