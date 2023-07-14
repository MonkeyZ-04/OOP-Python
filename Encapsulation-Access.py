#Public()
#Protected(_)
#Private(__)

class Employee: #Public

    def __init__(self,name,salary,department): 
        #public attribute
        self.name = name
        self.salary = salary
        self.department = department

    #public method
    def showData(self):
        print(f"Name : {self.name}")
        print("Salary : {}".format(self.salary))
        print(f"Department : {self.department}")

obj1 = Employee("Non",50000,"Accounting")
obj1.showData