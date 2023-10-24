import threading 
import time

def func(seconds):
    print(f"Sleeping by for {seconds} seconds")
    time.sleep(seconds)
time1=time.perf_counter() #perf counter is use for performance couter
# Normal code 
# func(4)
# func(2)
# func(1)



# Same code using threads
t1=threading.Thread(target=func,args=[4])
t2=threading.Thread(target=func,args=[2])
t3=threading.Thread(target=func,args=[1])
t1.start()
t2.start()
t3.start()


t1.join()
t2.join()
t3.join()
time2=time.perf_counter()
print(time2-time1)