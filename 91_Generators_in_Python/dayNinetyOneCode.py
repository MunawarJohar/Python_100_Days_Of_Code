def my_Generator():
    for i in range(10):
        yield i
        
gen=my_Generator()
# print(next(gen))
# print(next(gen))
# print(next(gen))

for j in gen:
    print(j)
