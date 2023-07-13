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
opj1 = Employee()
opj1.detail("Non",50000,"Accounting")
opj1.showData()

opj2 = Employee()
opj2.detail("Mon",120,"Duck")
opj2.showData()

opj3 = Employee()
opj3.detail("Nono",100000,"Ceo")
opj3.showData()