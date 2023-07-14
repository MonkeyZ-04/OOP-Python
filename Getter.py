class Employee:

    def __init__(self,name,salary,department): 
        self._name = name 
        self.__salary = salary 
        self.__department = department 

    def _showData(self):
        print(f"Name : {self._name}")
        print("Salary : {}".format(self.__salary))
        print("Department : {}"+self.getDepartment())

    # setter method
    def setName(self,newname):
        self._name = newname
    def setSalary(self,newsalary):
        self.__salary = newsalary
    def setDepartment(self,newdepartment):
        self.__salary = newdepartment
    #getter method
    def getName(self):
        return self._name
    def getSalary(self):
        return self.__salary
    def getDepartment(self):
        return self.__department

obj1 = Employee("Non",50000,"Accounting")
print(obj1.getName())
print(obj1.getSalary())
print(obj1.getDepartment())