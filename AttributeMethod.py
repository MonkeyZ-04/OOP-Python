# name , salary

class Employee: #build class
    #Build Method
    def detail(self):
        self.name = "Non"
        self.salary = "50000"
        print(f"Name : {self.name}")
        print("Salary : {}".format(self.salary))

# Build object
opj1 = Employee()
opj1.detail()
