#Inheritance
class Employee:
    #Class Variable
    minSalary = 12000
    maxSalary = 50000
    companyName = "XYZ จำกัด" 

    def __init__(self,name,salary,department): 
        # instance variable
        self.__name = name 
        self.__salary = salary 
        self._department = department 

    def _showData(self):
        print(f"Name : {self.__name}")
        print("Salary : {}".format(self.__salary))
        print(f"Department : {self._department}")

class Accounting(Employee):
    def __init__(self):
        pass

class Programmer(Employee):
    pass

class Sale(Employee):
    pass


account = Accounting()
print(account.companyName)
# programmer = Programmer()
# sale = Sale()