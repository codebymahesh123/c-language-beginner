def factorial():
    n= int(input("enter the number is : "))
    fact=1 
    for i in range(1,n+1):
        fact*=i
        print(f"factoraial of {i} is: ",fact)
factorial()