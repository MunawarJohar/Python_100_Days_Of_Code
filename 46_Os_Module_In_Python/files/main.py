import os

if(not os.path.exists("new")):
     os.mkdir("new")
  
for i in range(0,100):
    os.mkdir(f"new/day{i+1}")
    