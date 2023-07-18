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
    #salary per year
    def _getIncome(self):
        return self.__salary*12
    def __str__(self):
        return "Name = {} , Department = {}, Salary = {} , Salary per Year = {}".format(self.__name, self._department, self.__salary, self._getIncome())
class Accounting(Employee):
    __departmentName = "Accounting"
    def __init__(self,name,salary):
        super().__init__(name,salary,self.__departmentName)
        super()._showData()

class Programmer(Employee):
    __departmentName = "Programmer"
    def __init__(self,name,salary):
        super().__init__(name,salary,self.__departmentName)
        super()._showData()

class Sale(Employee):
    __departmentName = "Sale"
    def __init__(self,name,salary):
        super().__init__(name,salary,self.__departmentName)
        super()._showData()

account = Accounting("Non",35000)
print(account.__str__())
programmer = Programmer("Nini",50000)
print(programmer.__str__())
sale = Sale("NorNor",12000)
print(sale.__str__())