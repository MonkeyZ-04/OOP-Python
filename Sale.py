from Employee import Employee
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