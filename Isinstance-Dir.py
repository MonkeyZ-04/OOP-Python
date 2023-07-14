"""
isinstance => check where obj was build by class
 dir => show attribute and Method
 __class => show name of class and obj

"""
class Employee: 

    def __init__(self,name,salary,department): 
        self.name = name
        self.salary = salary
        self.department = department



    def showData(self):
        print(f"Name : {self.name}")
        print("Salary : {}".format(self.salary))
        print(f"Department : {self.department}")



obj1 = Employee("Non",50000,"Accounting")
obj2 = Employee("Mon",120,"Duck")
obj3 = Employee("Nono",100000,"Ceo")

print(isinstance(obj1,Employee))
print(dir(obj2))
print(obj3.__class__)