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
programmer = Programmer("Nini",50000)
sale = Sale("NorNor",12000)