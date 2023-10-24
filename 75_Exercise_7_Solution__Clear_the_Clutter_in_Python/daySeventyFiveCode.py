import os
files=os.listdir("ClutterFolder")
i=1
for file in files:
    if file.endswith(".PNG"):
     print(file)
    os.rename(f"ClutterFolder/{file}",f"ClutterFolder/{i}.PNG")
    i=i+1
    