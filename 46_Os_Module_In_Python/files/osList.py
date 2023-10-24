import os
print(f"My current working directory is :{os.getcwd}")
folders=os.listdir("new")
print(folders)

for folder in folders:
    print(folder)
    print(os.listdir(f"new/{folder}"))