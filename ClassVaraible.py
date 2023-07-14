#Class Variable
class Employee:
    #Class Variable
    _minSalary = 12000
    _maxSalary = 50000 

    def __init__(self,name,salary,department): 
        # instance variable
        self._name = name 
        self._salary = salary 
        self._department = department 

    def _showData(self):
        print(f"Name : {self._name}")
        print("Salary : {}".format(self._salary))
        print(f"Department : {self._department}")


obj1 = Employee("Non",50000,"Accounting")
print(Employee._minSalary)
print(Employee._name) #Error cause should have obj to access