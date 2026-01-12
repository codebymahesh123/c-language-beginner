with open("with.txt","r") as f:
    data=f.read()
    print(data)
f.close()

#delet a file code 
import os  # any file delet this delet file 
os.remove("with.txt")