# take any two nuber input sum,diffrence,product,qudenation
def sum():
    try:
        a=float(input("enter the number : "))
        b=float(input("enter the b : "))
        add=a+b
        print("total number are add is ",add)
        diffrence=a-b
        print("subtract is of number is ",diffrence)
        product=a*b
        print(f"multipy is  {product}")
        quiodent=a/b
        print(f"divided is {quiodent} ")
    except ValueError:
        print("enter the right value ! please !!")
sum()
