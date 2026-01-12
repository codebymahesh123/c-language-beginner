class bankaccount:
    def __init__(self,name,blancace): # this is public attribute
        self.name=name
        self.__blancace=blancace
    def get__blance(self):
        return self.__blancace
    
    def set_blance(self,newblance):
        self._blancace=newblance 

a1=bankaccount("mahesh",10_00000)
a1.set_blance(100000)
print(a1.set_blance)

print("my new balncer is = ",a1.set_blance)

print(" your name is =",a1.name)
print("your BLANCE IS =",a1.__blancace)


    