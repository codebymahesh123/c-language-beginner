from abc import ABC , adstractmethod       
class Animal(ABC):
    @adstractmethod
    def make_sound(self):
        pass

class Lion(Animal):
    def make_sound(self):
        print("Roar!") 
 
lion=Lion()
lion.make_sound()
