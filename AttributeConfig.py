# name , salary

class Employee: #build class
    #Build Method
    def detail(self,name,salary,department):
        self.name = name
        self.salary = salary
        self.department = department

    def showData(self):
        print(f"Name : {self.name}")
        print("Salary : {}".format(self.salary))
        print(f"Department : {self.department}")

# Build object
obj1 = Employee()
obj1.detail("Non",50000,"Accounting")
obj1.showData()

obj2 = Employee()
obj2.detail("Mon",120,"Duck")
obj2.showData()

obj3 = Employee()
obj3.detail("Nono",100000,"Ceo")
obj3.showData()