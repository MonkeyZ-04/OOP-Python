# Overloading
class Employee:
    # Class Variable
    minSalary = 12000
    maxSalary = 50000
    companyName = "XYZ จำกัด"

    def __init__(self, name, salary, department):
        # instance variable
        self.__name = name
        self.__salary = salary
        self._department = department

    def _showData(self):
        print(f"Name : {self.__name}")
        print("Salary : {}".format(self.__salary))
        print(f"Department : {self._department}")

    # salary per year
    def _getIncome(self,bonus=0,overtime=0):
        return (self.__salary * 12)+bonus+overtime

    def __str__(self):
        return "Name = {} , Department = {}, Salary = {} , Salary per Year = {}".format(self.__name, self._department,
                                                                                        self.__salary,
                                                                                        self._getIncome())


class Accounting(Employee):
    __departmentName = "Accounting"

    def __init__(self, name, salary, age):
        super().__init__(name, salary, self.__departmentName)
        self.__age = age

    def _showData(self):
        super()._showData()
        print(f"Age : {self.__age}")

    def __str__(self):
        return super().__str__() + ", Age = {}".format(self.__age)


class Programmer(Employee):
    __departmentName = "Programmer"

    def __init__(self, name, salary, experience, skill):
        super().__init__(name, salary, self.__departmentName)
        self.__exp = experience
        self.__skill = skill

    def _showData(self):
        super()._showData()
        print(f"Experience : {self.__exp}")
        print(f"Skill : {self.__skill}")

    def __str__(self):
        return super().__str__() + ", Experience = {} , Skill = {}".format(self.__exp, self.__skill)


class Sale(Employee):
    __departmentName = "Sale"

    def __init__(self, name, salary, area):
        super().__init__(name, salary, self.__departmentName)
        self.__area = area

    def _showData(self):
        super()._showData()
        print(f"Area : {self.__area}")

    def __str__(self):
        return super().__str__() + ", Area = {}".format(self.__area)


account = Accounting("Non", 35000, 30)
account._showData()
print(account.__str__())
print(f"Salary/Year With Bonus {account._getIncome(50_000)}")
programmer = Programmer("Nini", 50000, 2, "Dev Game")
programmer._showData()
print(programmer.__str__())
print(f"Salary/Year With Bonus {programmer._getIncome(80_000,8_000)}")
sale = Sale("NorNor", 12000, "CNX")
sale._showData()
print(sale.__str__())
