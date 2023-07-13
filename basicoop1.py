# name , salary

class Employee: #build class
    #Build Method
    def detail(self):
        self.name = "None"
        self.salary = "Infinity"
        print(f"Name : {self.name}")
        print("Salary : {}".format(self.salary))

# Build object
emp1 = Employee()
emp1.detail()