class Empolyee:
    start="4am"
    endtime="9pm"

    def change_time(self,new_endtime):
        self.endtime=new_endtime

class teachers (Empolyee):
    def __init__(self,subject):
        self.subject=subject

t1=teachers("math")
t1.change_time(" 5pm")
print(t1.subject,t1.start,t1.endtime)
