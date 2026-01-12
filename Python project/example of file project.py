def newfile():
    f= open("fileproject.txt","x")
    data=f.read()
    print(data)
    f.close()


def writefile():
    f=open("fileproject.txt","a")
    data=f.write("hello i am here this is my first\n project in\n this way\n for high ")
    print(data)
    f.close()
#start

data=True
line=1
word="python"
with open("fileproject.txt","r")as f:
    while data:
        data=f.readline()  #only 1st line read 
        if(word in data):
            print(f"{word} word is present  in line= {line}  !! ") # formatted string used 
            break
        print(data )
        line+=1

    





