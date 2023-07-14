# name , salary

class Employee: #build class
    #Build Method
    def detail(self):
        self.name = "Non"
        self.salary = "50000"
        print(f"Name : {self.name}")
        print("Salary : {}".format(self.salary))

# Build object
obj1 = Employee()
obj1.detail()
