import time

# print(time.time())
# def usingWhile():
#     i=0
#     while i<50:
#      i=i+1
#      print(i)
# def usingFor():
#     for i in range(100):
#         print(i)
# init=time.time()
# usingFor()
# print(time.time()-init)
# usingWhile
# print(6)
# time.sleep(3)
# print("This is print after 3 seconds")

t=time.localtime()
formatTime=time.strftime("%Y-%m-%d   %H:%M:%S",t)
print(formatTime)