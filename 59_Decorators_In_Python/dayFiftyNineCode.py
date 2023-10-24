
def greet(fx):
    def mfx(*args, **kwargs):
     print("Good morning")
     fx()
     print("Thank for using this function")
    return mfx

@greet
def hello(*args, **kwargs):
    print("Hello world")
    
def add(a,b):
    print(a+b)
    

#greet(hello)() #this is another method to called greet function
hello()
add(5,10)

# @decorator_function
# def my_function():
#     pass


# import logging
# def log_function(func):
#     def decorated(*args,**kwargs):
#         logging.info(f"{func.__name__} with args={args},kwargs={kwargs}")
#         result=func(*args,**kwargs)
#         logging.info(f"{func.__name}returned {result}")
#         return result
#     return decorated


# @log_function
# def my_function(a,b):
#     return a+b