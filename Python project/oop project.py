class product: # factorary product 
    count=0
    def __init__(self,name,price):
        self.name=name
        self.price=price
        product.count+=1

    def get_info(self):
        print(f"the price is {self.name} is Rs : {self.price}")

    @classmethod # this is classmetod 
    def get_count(cls):
        print(f"total product {cls.count}")

    @staticmethod # this is staticcmethod 
    def clas_discount(price,discount):
        print(f"The final price is {price-(price*discount/100)}")
        
p1=product("phone",100000)
p2=product("motorola",150000)
p3=product("macbook",999999)
p4=product("apple",1000)

product.get_count()
p1.clas_discount(p4.price,10)    
p2.clas_discount(p1.price,10)
    