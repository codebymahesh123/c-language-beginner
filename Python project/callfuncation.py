def factoraila():
    n = int(input("enter n: "))
    fact = 1
    for i in range( 1,n+1):
        fact *= i
        print("factorial = ", fact)
factoraila()
try :
    def sum():
        a=int((input("enter the value a :  ")))
        b=int((input("enter the value ofa b is :")))
        c=a*b
        d=a+b
        print(c)
        print(f"sum of a and b is : ={d}")
except ValueError:
    print("enter the integer value is right number !")
sum()