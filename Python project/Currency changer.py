def b():
    doller=float(input("enter the value of doller =  "))
    Ruppes=89.87
    total=float(doller*Ruppes)
    print(f"total indian Ruppes is  = {total} ")

def a():
    Ruppes=float(input("enter the india rupees = "))
    dollar=89.87
    total=float(Ruppes/dollar)
    print(f"your doller is  = {total}")

while True:
    d1=input("choise your currency \n Dollar=a \n INR=b \n  exit \n enter your choise = ")
    if(d1=="exit"):
        break
    match d1:
        case "b":
            a()
        case "a":
            b()
  
      
        

