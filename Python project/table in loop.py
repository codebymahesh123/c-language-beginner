# using loop while 
try:
    table=int(input("enter the table "))
    x=1
    while(x<=10):  
        print(table*x) #tabel*1=1 2*2=4 
        x+=1
    
except ValueError:
    print("please enter integer value ! : ")

    