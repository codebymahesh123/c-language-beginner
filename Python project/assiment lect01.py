#Write a program that asks  theuserfortheir name  andage,then  print sasentence   like

name=input("enter the your name : ")
try:
    age=int(input("enter the age "))
    print(f"hello !  {name} you are {age} years old ") # formated strin used 
except ValueError:
    print("pleser enter the interger value !")
    



        
    
    






