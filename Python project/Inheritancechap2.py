class Employee:
    start_time="10am"
    end_time="8pm"

class AdminStaff(Employee):
    def __init__(self,role):
        self.role = role

class Accontants(AdminStaff):
    def __init__(self,salary,role):
        super().__init__(role)
        self.salary=salary
    
acc1=Accontants(293_0000,"manggeres")
print(acc1.role,acc1.salary,acc1.start_time,acc1.end_time)
print(acc1.start_time,acc1.end_time)
print(acc1.salary)