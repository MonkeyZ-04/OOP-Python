#Public()
#Protected(_)
#Private(__)

class Employee: #Public

    def __init__(self,name,salary,department): 
    #Private attribute
        self._name = name #Protected
        self.__salary = salary #Private
        self.__department = department #Private
        self.__showData()

    #Private method
    def __showData(self):
        print(f"Name : {self._name}")
        print("Salary : {}".format(self.__salary))
        print(f"Department : {self.__department}")


obj1 = Employee("Non",50000,"Accounting")
obj1._name = "Nini"
obj1.__salary = 100
# obj1.__showData()