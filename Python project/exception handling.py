 
try:
    x=int(input("enter the numbr is  = "))
    ans=10/x
except ZeroDivisionError:
    print(f"divided by zero is not allwed  ")
except ValueError:
    print("plese enter intger value  !!")

else:
    print(ans)
finally:
    print("the end")


    