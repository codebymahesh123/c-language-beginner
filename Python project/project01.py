# daba cooking menu chart
# using dictonary in chart 
try:
    menu={
    'pizza':50,
    'pasta':100,
    "burger":50,
    "salad":50,
    "dal":100,
    "apple":200,
    "masala":400,
    }


    #great 
    print("welcome to my Daba this is best Daba in this street")
    print("my Daba  menu is here = \n pizza : 100\n buger : 50 \n salad : 50 \n dal : 100 \n apple :100 \n pizza :100 \n masala : 400  ")
    order_total=0
    item_1=input("enter the of the item is = : ")

   

    # Membership opreter using
    if(item_1 in menu):
        print("this item is ablavial  in menu plase order to : ")

    
    order_total += menu[item_1]
    another_order=input("than you order to anothert item is (yes/no)")
    if another_order=="yes":
        item_2=input("enter the other order : ")
    elif another_order=="no":
        print("ok thanks !!!r")
    
    print(f"your total order is Rs= {order_total}")
    print("thank for vesting for My daba ..")


except ValueError:
    print("please enter the right value in chart!! ")

    

