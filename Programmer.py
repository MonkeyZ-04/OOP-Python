from Employee import Employee
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
