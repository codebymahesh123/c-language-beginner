
def dic():
    dictonary={"name": "mahesh maurya", #keys : value 
               "student": " b.tech cse students ",
               "cgpa": " 8.5",
               "subject": "math,python,c++and c language",
               3.143 : "pi value "
    }
    print(dictonary.keys())
    print(dictonary.values())
    print(dictonary.items())
    print(dictonary["name"])
    print(dictonary[3.143]) # it not using in long code crash the code 
    print(dictonary.get("name")) # worng key to code its run it  it using this  that ansewe in none 
    print("end of code !!")
    dictonary.update({"collage":"IIt bhu varanasi"})
    print(dictonary)
dic()
def sum(a,b):
    s=a+b
    print(s)
ans=sum(3,4)
print(ans)
