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

