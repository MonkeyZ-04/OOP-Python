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
    __departmentName = "Account"
    def __init__(self):
        pass

class Programmer(Employee):
    __departmentName = "Programmer"
    def __init__(self):
        pass

class Sale(Employee):
    __departmentName = "Sale"
    Salary = 20000
    def __init__(self):
        pass



account = Accounting()
print(account.companyName)
programmer = Programmer()
print(programmer.maxSalary)
sale = Sale()
print(sale.Salary)