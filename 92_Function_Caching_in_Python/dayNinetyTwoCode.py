from functools import lru_cache
import time

@lru_cache(maxsize=None)

def fx(n):
    time.sleep(5)
    return n*5

print(fx(20))
print("Done for 20") 

print(fx(2))
print("Done for 2") 

print(fx(5))
print("Done for 5") 

# it used the term memoization.
# do not fetch the values from catch again 
print(fx(20))
print("Done for 20") 

print(fx(2))
print("Done for 2") 

print(fx(5))
print("Done for 5") 