class students:
        def __init__ (self,car,cgpa,model):
            self.car=car
            self.cgpa=cgpa
            self.model=model
        def get_cgpa(self):
              return self.cgpa                               
        def get_model(self):
              return self.model
        

car2=students("mahindra",5.6,"toyata ")
car3=students("range rover",4.4,"hink")
car4=students("maherrr",45.5,"harru  chaina ")


print(car2.car)
print(car3.cgpa)
print(car2.get_cgpa())
print(f"this is chanees best brand in china  :  ",car4.get_model())




    