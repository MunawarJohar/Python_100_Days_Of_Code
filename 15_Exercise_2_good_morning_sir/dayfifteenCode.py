import time
timestamp=int(time.strftime('%H'))
print(timestamp)
if(timestamp<9):
    print("Good Morning Sir :")
elif(timestamp>=10 and timestamp <= 3):
    print("Good afternoon Sir")
else:
    print("Good Evening")