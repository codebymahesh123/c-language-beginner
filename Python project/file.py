f=open("sample.txt","r") #reading this file  see the file what the write 
data=f.read()
print(data)
f.close()

def writting(): # writting the file so actual write file change 
    d=open("sample1.txt","w")
    data=d.write("mahesh \n maurya hello i am\n mahesh majuray   \norkforgjvofdv  \n  ")
    print(data)
    d.close()
writting()

def new():
    new=open("sample1.txt","a")
    data=new.write("\n start line \nheloo i am here please !! write here ")
    print(data)
    new.close()
new()

def newfile():
    newfile=open("sample2.txt","w") # x is using to create a file in py 
    data=newfile.write("this is new file create thso \n hello line 2 ")
    print(data)
    newfile.close()


def newfile():
    newfile=open("sample2.txt","a") # a is append the file inculed file 
    newfile.write("\n this my line new line hello this for you ")
    print(newfile)
    newfile.close()
newfile()



